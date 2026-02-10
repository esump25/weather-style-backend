import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows your frontend to talk to this backend

# The secret API Key will be read from Render's environment variables
OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY')

@app.route('/suggest', methods=['POST'])
def get_suggestion():
    data = request.get_json()
    city = data.get('city')

    if not city:
        return jsonify({"error": "No city provided"}), 400

    # 1. Get weather from OpenWeatherMap
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=imperial"
    
    try:
        response = requests.get(weather_url)
        weather_data = response.json()

        if response.status_code != 200:
            return jsonify({"error": "City not found"}), 404

        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        # 2. Logic: What to wear?
        if temp <= 32:
            suggestion = "It's freezing! Wear a heavy parka, thermal layers, and a scarf."
        elif temp <= 55:
            suggestion = "Chilly out. A warm jacket or a wool coat is a must."
        elif temp <= 70:
            suggestion = "Mild weather. A light sweater or a denim jacket should do."
        else:
            suggestion = "It's warm! T-shirt and shorts weather."

        return jsonify({
            "city": city,
            "temp": temp,
            "description": description,
            "suggestion": suggestion
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)