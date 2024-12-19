import streamlit as st
import folium
import sqlite3
from streamlit_folium import st_folium
from datetime import datetime
import base64
from geopy.geocoders import Nominatim
from folium.plugins import LocateControl
import os
import base64

def init_db():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()

    # Create tables
    c.execute('''CREATE TABLE safe_locations
                 (latitude REAL, longitude REAL, capacity INTEGER, status TEXT, type TEXT)''')

    c.execute('''CREATE TABLE alerts
                 (type TEXT, description TEXT, timestamp DATETIME)''')

    c.execute('''CREATE TABLE disaster_zones
                 (latitude REAL, longitude REAL, intensity TEXT, description TEXT)''')

    # Sample data - Safe locations including medical facilities
    safe_locations = [
        (12.9716, 77.5946, 50, 'Available', 'shelter'),
        (12.9352, 77.6245, 30, 'Available', 'shelter'),
        (12.9452, 77.6045, 100, 'Available', 'medical'),
        (12.9552, 77.5845, 80, 'Available', 'medical')
    ]
    
    c.executemany("INSERT INTO safe_locations VALUES (?, ?, ?, ?, ?)", safe_locations)

    # Sample alerts
    alerts = [
        ('Earthquake Warning', 'Magnitude 5.2 earthquake detected 50km away. Stay alert and prepare for aftershocks.', 
         datetime.now()),
        ('Weather Alert', 'Heavy rainfall expected in your area. Potential for flooding in low-lying areas.', 
         datetime.now())
    ]
    
    c.executemany("INSERT INTO alerts VALUES (?, ?, ?)", alerts)

    conn.commit()
    return conn

def get_zone_color(intensity):
    return {
        'high': 'red',
        'medium': 'orange',
        'low': 'green'
    }.get(intensity, 'gray')

def get_location():
    try:
        geolocator = Nominatim(user_agent="disaster_guard")
        loc = geolocator.geocode(st.session_state.get('address', ''))
        if loc:
            return loc.latitude, loc.longitude
        return None
    except:
        return None

def create_map(conn):
    c = conn.cursor()
    locations = c.execute("SELECT * FROM safe_locations").fetchall()

    # Get user's location (default to Bangalore if not available)
    user_location = get_location() or (12.9716, 77.5946)
    
    # Create base map centered on user's location
    m = folium.Map(location=user_location, zoom_start=12)
    
    # Add locate control
    LocateControl().add_to(m)

    # Add user's location as blue marker
    folium.Marker(
        location=user_location,
        popup="Your Location",
        icon=folium.Icon(color='blue', icon='user')
    ).add_to(m)

    # Add safe locations with different icons for shelters and medical facilities
    for loc in locations:
        icon_color = 'green' if loc[4] == 'shelter' else 'red'
        icon_type = 'home' if loc[4] == 'shelter' else 'plus'
        folium.Marker(
            location=[loc[0], loc[1]],
            popup=f"Type: {loc[4].title()}<br>Capacity: {loc[2]}<br>Status: {loc[3]}",
            icon=folium.Icon(color=icon_color, icon=icon_type)
        ).add_to(m)

    # Add disaster zones
    zones = [
        (12.9716, 77.5946, 'high', 'Severe Flooding'),
        (12.9452, 77.6145, 'medium', 'Strong Winds'),
        (12.9333, 77.6100, 'low', 'Heavy Rainfall')
    ]

    for zone in zones:
        folium.Circle(
            location=[zone[0], zone[1]],
            radius=1000,
            color=get_zone_color(zone[2]),
            fill=True,
            popup=f"Status: {zone[3]}<br>Intensity: {zone[2].capitalize()}"
        ).add_to(m)

    return m

def get_safety_guide_download_link():
    file_path = "pocket-guide.pdf" 

    if os.path.exists(file_path):
        with open(file_path, "rb") as pdf_file:
            b64 = base64.b64encode(pdf_file.read()).decode()

        # Return the HTML download link
        return f'<a href="data:application/pdf;base64,{b64}" download="safety_guide.pdf">Download Safety Guide</a>'
    else:
        return "Error: Safety guide PDF not found in the directory."

def render_family_form():
    st.subheader("👥 Family Details Form")
    
    # Back button
    if st.button("← Back to Home"):
        st.session_state.page = "main"
        return

    family_size = st.number_input("Number of family members:", min_value=1, step=1)
    family_data = []

    for i in range(family_size):
        with st.container():
            name = st.text_input(f"Name of family member {i+1}:", key=f"name_{i}")
            location = st.text_input(f"Location of family member {i+1}:", key=f"location_{i}")
            family_data.append((name, location))

    if st.button("Submit"):
        st.success("Family details submitted successfully!")
        st.session_state.page = "main"

def render_safe_locations_form():
    st.subheader("📍 Report Safe Location")
    
    # Back button
    if st.button("← Back to Home"):
        st.session_state.page = "main"
        return

    # Get current location
    address = st.text_input("Enter your current address:")
    if address:
        st.session_state.address = address
        location = get_location()
        if location:
            st.success(f"Location found: {location}")
            
            capacity = st.number_input("Estimated capacity (number of people):", min_value=1, step=1)
            
            if st.button("Submit Safe Location"):
                conn = init_db()
                c = conn.cursor()
                c.execute("INSERT INTO safe_locations VALUES (?, ?, ?, ?, ?)", 
                         (location[0], location[1], capacity, 'Available', 'shelter'))
                conn.commit()
                st.success("Safe location reported successfully!")
                st.session_state.page = "main"
        else:
            st.error("Could not find location. Please enter a valid address.")

import streamlit.components.v1 as components

def get_current_location():
    # Create a component for getting geolocation
    loc_html = """
    <div id="location-data"></div>
    <script>
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition(
                function(position) {
                    document.getElementById("location-data").innerHTML = 
                        position.coords.latitude + "," + position.coords.longitude;
                },
                function(error) {
                    document.getElementById("location-data").innerHTML = "error:" + error.message;
                }
            );
        } else {
            document.getElementById("location-data").innerHTML = "error:Geolocation not supported";
        }
    </script>
    """
    components.html(loc_html, height=0)

def render_panic_button():
    st.subheader("🚨 Emergency Alert")
    
    if st.button("← Back to Home"):
        st.session_state.page = "main"
        return

    st.warning("This will alert emergency services with your current location.")
    
    # Get GPS location automatically
    get_current_location()
    
    # Add location status indicator
    with st.status("📍 Getting your location...") as status:
        # Here you would check the location data from the browser
        # For now, we'll simulate a success
        status.update(label="📍 Location acquired", state="complete")
        
    emergency_type = st.selectbox("Emergency Type:", 
                                ["Medical Emergency", "Fire", "Natural Disaster", "Other"])
    
    description = st.text_area("Brief description of the emergency:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🚨 SEND EMERGENCY ALERT", 
                    type="primary",
                    use_container_width=True):
            st.success("Emergency alert sent successfully! Emergency services have been notified.")
            st.info("Stay calm. Help is on the way.")
            
    with col2:
        if st.button("Return to Home", use_container_width=True):
            st.session_state.page = "main"

def render_ai_doctor():
    st.subheader("🏥 AI Medical Assistant")

    # Button to show chatbot
    if st.button("Get Medical Advice"):
        chatbot_iframe = """
        <iframe src="https://cdn.botpress.cloud/webchat/v2.2/shareable.html?configUrl=https://files.bpcontent.cloud/2024/12/19/09/20241219090710-RX0SNENO.json"
                width="100%" height="600" style="border:none;">
        </iframe>
        """
        # Render the iframe
        st.components.v1.html(chatbot_iframe, height=650)            

def render_emergency_kit():
    st.subheader("🎒 Emergency Kit Checklist")
    kit_data = {
        "Basic Supplies": [
            "Water (one gallon per person per day)",
            "Non-perishable food (3-day supply)",
            "Battery-powered radio",
            "Flashlight and batteries"
        ],
        "Medical Items": [
            "Prescription medications",
            "First aid kit",
            "First aid reference guide"
        ],
        "Tools and Supplies": [
            "Multi-tool or basic tools",
            "Manual can opener",
            "Cell phone with chargers",
            "Important documents in waterproof container"
        ]
    }

    for category, items in kit_data.items():
        st.write(f"### {category}")
        for item in items:
            st.checkbox(item, key=f"kit_{item}")

def main():
    # Set page config
    st.set_page_config(page_title="DisasterGuard", layout="wide")

    # Initialize database
    conn = init_db()

    # Initialize session state for navigation
    if "page" not in st.session_state:
        st.session_state.page = "main"

    # Render appropriate page
    if st.session_state.page == "main":
        # Custom CSS
        st.markdown("""
            <style>
            .main-header {color: #ff4b4b;}
            .stButton>button {
                width: 100%;
                background-color: #000000;
                color: white;
                border-radius: 10px;
                padding: 15px;
            }
            .emergency-button>button {
                background-color: #ff4b4b !important;
            }
            .action-card {
                padding: 20px;
                border-radius: 10px;
                background-color: white;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }
            .icon-display {
                font-size: 24px;
                margin-bottom: 10px;
            }
            </style>
        """, unsafe_allow_html=True)

        # Header with logo
        st.markdown("# ⚠️ DisAstra")

        # Main action buttons
        cols = st.columns(4)

        with cols[0]:
            if st.button("🚨 PANIC BUTTON", key="panic"):
                st.session_state.page = "panic"

        with cols[1]:
            if st.button("👥 Family Details", key="family"):
                st.session_state.page = "family_form"

        with cols[2]:
            if st.button("📍 Safe Locations", key="safe_locations"):
                st.session_state.page = "safe_locations"

        with cols[3]:
            guide_data = get_safety_guide_download_link()
            if guide_data:
                st.download_button(
                    label="📥 Download Safety Guide",
                    data=guide_data,
                    file_name="safety_guide.pdf",
                    mime="application/pdf"
                )
            else:
                st.error("Safety guide PDF not found. Please ensure it is in the correct directory.")


        # Main content area
        col1, col2 = st.columns([2, 1])

        with col1:
            tab1, tab2, tab3 = st.tabs(["Emergency Map", "AI Doctor", "Emergency Kit"])

            with tab1:
                st.subheader("Emergency Map")
                map_data = create_map(conn)
                st_folium(map_data, width=800)

            with tab2:
                render_ai_doctor()

            with tab3:
                render_emergency_kit()

        with col2:
            st.subheader("Active Alerts")
            c = conn.cursor()
            alerts = c.execute("SELECT * FROM alerts").fetchall()

            for alert in alerts:
                with st.container():
                    st.markdown(f"""
                        <div style='padding: 15px; border: 1px solid #ddd; border-radius: 10px; margin-bottom: 15px;'>
                            <h4 style='color: #ff4b4b; margin-top: 0;'>⚠️ {alert[0]}</h4>
                            <p style='margin-bottom: 0;'>{alert[1]}</p>
                        </div>
                    """, unsafe_allow_html=True)

            # Mental Health Support Section
            st.subheader("🌿 Mental Health Support")
            if st.button("Start Breathing Exercise"):
                st.write("Follow the breathing pattern:")
                st.write("Breathe in: 4 seconds")
                st.write("Hold: 4 seconds")
                st.write("Breathe out: 4 seconds")

            st.write("### 24/7 Support Hotlines")
            st.write("National Crisis Hotline: 1800 233 3330")

    elif st.session_state.page == "family_form":
        render_family_form()
    elif st.session_state.page == "safe_locations":
        render_safe_locations_form()
    elif st.session_state.page == "panic":
        render_panic_button()

if __name__ == "__main__":
    main()