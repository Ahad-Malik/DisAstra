Got it! Here's the updated **README** with proper acknowledgment for the participants:

---

# DisAstra - Real-time Emergency Management App

**DisAstra** is a powerful web-based platform built to provide life-saving support in disaster situations. The app offers real-time safety information, emergency alerts, and practical guidance to individuals and families during emergencies. Using cutting-edge geolocation and mapping technologies, DisAstra helps users identify safe locations, report hazards, send emergency alerts, and access critical resources. From AI-driven medical advice to mental health support, DisAstra ensures you are never alone in times of crisis.

---

## 🌟 Key Features

### 1. **Emergency Map**
   - **Interactive Map:** See real-time safe locations (shelters, medical facilities, etc.) around you.
   - **Disaster Zones:** Visualize zones affected by disasters such as floods, strong winds, and fires with color-coded intensity markers.
   - **Current Location:** The map auto-centers on your live location with blue markers for easy identification.
   - **Real-Time Location Tracking:** The map updates in real time, allowing you to track and find nearby safe areas.

### 2. **AI Medical Assistant**
   - **Instant Medical Advice:** Get life-saving medical advice powered by AI through an interactive chatbot.
   - **Emergency Symptoms Analysis:** Ask questions about symptoms, conditions, or health concerns in real time.

### 3. **Panic Button**
   - **Send Emergency Alerts:** Instantly send alerts with your current location to emergency responders.
   - **Customizable Alerts:** Specify emergency types (Medical, Fire, Natural Disaster) with a description for first responders.

### 4. **Safe Location Reporting**
   - **Report Safe Zones:** Mark safe shelters or medical facilities and their available capacity.
   - **Track Status:** View the status of reported safe locations (Available, Full, etc.) in real-time.

### 5. **Family Details Form**
   - **Family Tracking:** Quickly enter family member names and locations for easy tracking in case of emergency.
   - **Keep Everyone Safe:** Share family details and have them stored securely for emergency situations.

### 6. **Emergency Kit Checklist**
   - **Survival Essentials:** Checklist of essential items like water, food, first aid kits, flashlights, and more.
   - **Pre-pack your kit:** Mark off what you have ready for an emergency and check off as you prepare.

### 7. **Active Alerts**
   - **Real-Time Disaster Alerts:** Get notified with alerts about ongoing disasters (earthquakes, storms, floods).
   - **Weather Warnings & Updates:** Keep track of severe weather events and prepare accordingly.

### 8. **Mental Health Support**
   - **Breathing Exercises:** Access guided breathing exercises to calm your nerves during stressful times.
   - **Crisis Hotlines:** View emergency mental health support hotlines for immediate assistance.

### 9. **Downloadable Safety Guide**
   - **Pocket Safety Guide:** Download a handy PDF with disaster preparedness information and tips.
   - **Essential Steps:** Ensure you have all the necessary info at hand when disaster strikes.

---

## 🚀 Installation

To get started with DisAstra, follow these simple steps to install and run the app:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/disastra.git
   cd disastra
   ```

2. **Install dependencies:**
   - Make sure you have Python 3.x installed on your system.
   - Install required libraries with:
     ```bash
     pip install -r requirements.txt
     ```

3. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

Once the app is running, open your browser and navigate to `localhost:8501` to start using DisAstra.

---

## 🛠 Key Libraries

- **Streamlit:** For creating the interactive user interface (UI).
- **Folium:** For displaying geospatial maps and disaster zones.
- **SQLite:** For storing data like safe locations, disaster alerts, and reports.
- **Geopy:** To integrate location-based services.
- **Streamlit-Folium:** For embedding Folium maps directly in the Streamlit app.
- **Base64:** For embedding safety guide downloads and other media directly.

---

## 💡 How It Works

### Main Screen
   - Upon launching the app, users are greeted with a clean and intuitive dashboard. From here, they can navigate through options like accessing the panic button, entering family details, and viewing nearby safe locations.
   - Navigation is simple and seamless, with each option clearly laid out for easy use during emergencies.

### Emergency Map
   - The map is centered around your current location and updates in real time.
   - You can zoom in or out to check nearby **safe zones**, **hospitals**, **shelters**, and **disaster areas** marked with color-coded circles that represent different **disaster intensities** (high, medium, low).
   - **Disaster zones** show details such as intensity (e.g., flood, earthquake), while **safe locations** display their type (shelter, medical), capacity, and availability status.

### Panic Button
   - In case of an emergency, users can quickly trigger the **panic button**.
   - It instantly shares the user’s current location along with the emergency type (medical, fire, disaster) with local emergency responders.

### AI Medical Assistant
   - Need medical advice or have health concerns? Our AI chatbot provides quick responses to medical queries, helping you make informed decisions during stressful times.
   - Perfect for minor injuries, first aid tips, or medical emergencies where immediate attention is required.

### Safe Location Reporting
   - If you are at a **safe location** or have found one (such as a shelter or medical facility), you can report its details (location, capacity, and type) for others to view.
   - Users can also update the status of reported safe locations, ensuring others know whether the area is available or full.

### Family Details Form
   - In emergencies, it's crucial to have up-to-date contact and location information for your family members.
   - Use the **Family Details Form** to securely record names, locations, and contact info for all family members, ensuring you can reach them quickly during a crisis.

### Emergency Kit Checklist
   - Preparing in advance is key to survival during disasters. With **Emergency Kit Checklist**, you can easily track what you already have and what needs to be packed, like:
     - Water
     - Non-perishable food
     - Flashlights
     - First Aid Kits
     - Emergency blankets
     - And much more!

### Active Alerts
   - DisAstra keeps you up-to-date on ongoing **disaster alerts**.
   - Stay informed about weather warnings, earthquakes, or fire outbreaks, and know exactly when and where to take action.

### Mental Health Support
   - Disasters can be mentally taxing. Use **breathing exercises** to reduce stress and anxiety during intense moments.
   - Reach out to **24/7 mental health crisis hotlines** for support during stressful times.

### Safety Guide Download
   - Access a **pocket-sized safety guide** to have essential emergency information at your fingertips.
   - This guide includes survival tips, disaster prep steps, and first aid instructions.

---

## 📸 Screenshots

![Main Page](screenshots/main_page.png)

![Emergency Map](screenshots/emergency_map.png)

![Panic Button](screenshots/panic_button.png)

---

## ⚙️ Technology Stack

- **Frontend:** Streamlit for building a user-friendly interface.
- **Backend:** SQLite for storing dynamic data, such as alerts and safe location information.
- **Mapping:** Folium for interactive map rendering.
- **Geolocation:** Geopy for location tracking and geospatial data.
- **Emergency Alerts:** SQLite to manage real-time alerts.

---

## 🤝 Contributing

We welcome contributions to make DisAstra even more helpful for users in crisis situations. If you find any issues, have feature ideas, or want to improve existing code, feel free to submit a pull request!

### How to Contribute:
1. **Fork the repository** to your own GitHub account.
2. **Clone the repository** to your local machine.
3. **Create a new branch** for your changes.
4. **Commit your changes** and push them to your forked repository.
5. **Create a pull request** to submit your changes.

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Contributors

This project was created by the following amazing developers:

- [Rayyan Khan](https://github.com/Rayyankhan18)
- [Parveez](https://github.com/Parveez7)
- [Ahad Malik](https://github.com/Ahad-Malik)

---

_DisAstra_ is designed with your safety in mind, aiming to provide all the tools you need to stay informed and prepared in emergency situations. Together, we can face any disaster, stay safe, and save lives.

**Stay Prepared. Stay Safe. Stay Strong.** 🚨

--- 

This version of the README gives credit to the contributors and provides a structured, engaging overview of the project. Let me know if you'd like any further adjustments!
