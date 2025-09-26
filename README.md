# 🌍 Weather API Project

A vibrant and modern Python project that fetches **real-time weather data** from the [OpenWeatherMap API](https://openweathermap.org/) with flair! 🌦️ Powered by sleek design and intuitive functionality, this project is your ticket to mastering APIs with style.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/License-MIT-green?logo=open-source-initiative" alt="MIT License">
  <img src="https://img.shields.io/badge/OpenWeatherMap-API-orange?logo=weather" alt="OpenWeatherMap API">
</p>

---

## What's This About?

This project is a **fun and educational** dive into working with APIs in Python. Here's what you'll master:

- 🌐 **API Integration**: Make HTTP requests like a pro
- 🔒 **Secure Secrets**: Manage API keys with `.env`
- 🛠️ **Virtual Environments**: Keep your project clean with `venv`
- 📋 **Dependency Management**: Organize packages with `requirements.txt`

---

## 📁 Project Structure

```
my-weather-app/
├── src/
│   └── weather.py        # Core script for fetching weather data
├── .env               # API key (kept secret with .gitignore)
├── .env.example       # Template for environment variables
├── requirements.txt   # Python dependencies
├── README.md          # You're reading this masterpiece!
├── .gitignore         # Ignores .env and venv
├── .venv/            # Virtual environment (not in repo)
```

---

## Get Started

Let's get this project up and running in a flash! ⚡ Follow these steps:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/my-weather-app.git
cd my-weather-app
```

### 2️⃣ Set Up a Virtual Environment

Keep your dependencies tidy with a virtual environment:

```bash
python -m venv .venv
```

**macOS/Linux**:

```bash
source .venv/bin/activate
```

**Windows (PowerShell)**:

```bash
.venv\Scripts\Activate.ps1
```

### 3️⃣ Install Dependencies

Grab the required packages with a single command:

```bash
pip install -r requirements.txt
```

### 4️⃣ Get an OpenWeatherMap API Key

- Sign up for a free account on [OpenWeatherMap](https://openweathermap.org/)
- Head to **API Keys** in your profile
- Copy your shiny API key

### 5️⃣ Configure the `.env` File

Create a `.env` file in the project root and add your API key:

```bash
WEATHER_API_KEY=your_api_key_here
```

**Security Note**: The `.env` file is ignored by Git to keep your API key safe. Use `.env.example` to share placeholders.

---

## How to Use It

Run the script with a city name to get a beautifully formatted weather update:

```bash
python src/weather.py London
```

### Sample Output

```
☁️ Weather in London: Scattered clouds
🌡️ Temperature: 18°C
💧 Humidity: 65%
🌬️ Wind Speed: 3.5 m/s
```

---

## Run Tests

Want to add some tests? Here's how to set up `pytest`:

```bash
pip install pytest
pytest -q
```

---

## Dependencies

- **[requests](https://pypi.org/project/requests/)** 📡: Simplifies HTTP requests
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** 🔐: Loads `.env` secrets securely

<p align="center">
  <img src="https://img.shields.io/pypi/v/requests?label=requests&color=blue" alt="requests version">
  <img src="https://img.shields.io/pypi/v/python-dotenv?label=python-dotenv&color=green" alt="python-dotenv version">
</p>

---

## Future Enhancements

Take this project to the next level with these exciting ideas:

- **Error Handling**: Gracefully handle invalid city names
- **Multi-City Support**: Fetch weather for multiple cities at once
- **Data Storage**: Save results to a CSV or SQLite database
- **Web API**: Build a Flask or Django API for a web-based interface

---

## About the Author

**Kwame Boateng**  
A passionate coder weaving tech and creativity together!  

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="#"><img src="https://img.shields.io/badge/Medium-12100E?logo=medium&logoColor=white" alt="Medium"></a>
  <a href="#"><img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white" alt="GitHub"></a>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Built%20with-%E2%9D%A4%EF%B8%8F-red" alt="Built with Love">
</p>

**Crafted with passion for coding and learning!** Let's make weather apps that shine! 