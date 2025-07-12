from flask import Flask, request, jsonify, render_template
import requests
import datetime
import pytz
import re

app = Flask(__name__, template_folder="templates")

# Your OpenRouter API details
API_KEY = "your-openrouter-api-key"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Weather API (OpenWeatherMap)
WEATHER_API_KEY = "your-openweathermap-api-key"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    language = data.get("language", "en-US")

    print(f"User said: {user_message} | Language: {language}")

    # Check if it's a weather-related query
    if "weather" in user_message.lower():
        city = extract_city(user_message)
        if city:
            return get_weather_response(city)
        else:
            return jsonify({"reply": "Please mention the city to get the weather update."})

    # If not a weather query, use OpenRouter API
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "anthropic/claude-3-haiku",
        "messages": [
            {"role": "system", "content": f"Respond clearly in the user's language: {language}."},
            {"role": "user", "content": user_message}
        ],
        "max_tokens": 200
    }

    try:
        response = requests.post(API_URL, headers=headers, json=body)
        response.raise_for_status()
        result = response.json()
        bot_reply = result["choices"][0]["message"]["content"]
        return jsonify({"reply": bot_reply.strip()})

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"reply": "Sorry, something went wrong while processing your request."})

@app.route("/info", methods=["GET"])
def get_info():
    tz = pytz.timezone("Asia/Kolkata")
    now = datetime.datetime.now(tz)
    current_time = now.strftime("%I:%M %p")
    current_date = now.strftime("%A, %d %B %Y")
    return jsonify({
        "time": current_time,
        "date": current_date
    })

# --- Weather Helper Functions ---

def extract_city(message):
    """
    Extracts a city name from a message using basic heuristics.
    You can improve this using NLP if needed.
    """
    match = re.search(r"in (\w+(?: \w+)?)", message.lower())
    if match:
        return match.group(1).strip().title()
    return None

def get_weather_response(city):
    """
    Gets the weather for a given city and returns JSON.
    """
    try:
        params = {
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": "metric"
        }
        res = requests.get(WEATHER_URL, params=params)
        data = res.json()

        if data.get("cod") != 200:
            return jsonify({"reply": f"Could not retrieve weather for {city}."})

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        reply = (f"Weather in {city}:\n"
                 f"- Condition: {weather.capitalize()}\n"
                 f"- Temperature: {temp}°C\n"
                 f"- Humidity: {humidity}%\n"
                 f"- Wind Speed: {wind_speed} m/s")

        return jsonify({"reply": reply})

    except Exception as e:
        print("❌ Weather API Error:", e)
        return jsonify({"reply": "Sorry, couldn't fetch the weather information right now."})

if __name__ == "__main__":
    app.run(debug=True)
