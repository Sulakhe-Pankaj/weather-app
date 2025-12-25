# Weather App 🌦️

A live weather web app built with **Flask (Python)** and powered by **OpenWeatherMap API**.
Search for any city and view real-time weather details with an animated, interactive UI and video background.

## 🚀 Features

* 🔎 **Search by City Name** – instantly fetch weather data
* 🌡️ **Current Conditions** – temperature, humidity, pressure, wind speed, weather description
* 💾 **Default City Load** – shows **Delhi weather on first visit**
* ⚠️ **Error Display** – shows error box on invalid/wrong city input
* 🎥 **Video Background** – full screen looping video behind content
* ✨ **Animated UI** – floating labels, shimmer input, pulse button, hover reactive weather card
* 📱 **Responsive Layout** – centered design works on desktop and mobile

## 🛠 Tech Stack

* **Backend:** Flask (Python)
* **Styling:** CSS Animations
* **API Provider:** OpenWeatherMap
* **HTTP Client:** Requests
* **Server:** Gunicorn
* **Deployment:** Render (Free Tier)

## ⚡ Installation (Local Run)

Clone the repo and install dependencies:

```bash
git clone https://github.com/Sulakhe-Pankaj/weather-app.git
cd weather-app
pip install -r requirements.txt
python app.py
```

## 🔑 Environment Variables (Render Dashboard)

Add this in Render project settings:

```
API_KEY=yuor api
```

## 🌍 Usage

* Enter a city name in the search bar
* View real-time weather output card
* Wrong city → error box appears
* First load always shows Delhi weather

## 🌐 Demo

* **Live App:** https://weather-app-z0ax.onrender.com

## 🤝 Contributing

* Fork the repo
* Create a new branch (`git checkout -b feature-name`)
* Commit your changes
* Push and open a PR

## 📬 Contact

* Name: Pankaj Sulakhe
* Email: pankajsulakhe76@gmail.com
* GitHub: Sulakhe-Pankaj
* Live App: https://weather-app-z0ax.onrender.com
