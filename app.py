from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app)

API_KEY = os.environ.get('OPENWEATHER_API_KEY')

@app.route('/suggest', methods=['POST'])
def suggest():
    data = request.get_json()
    city = data.get('city')
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    res = requests.get(url).json()

    if res.get("cod") != 200:
        return jsonify({"error": "City not found"}), 404

    temp = res['main']['temp']
    
    # Matching your aesthetic with specific labels
    if temp < 45:
        outfit = "editorial_cold.jpg"
        msg = "Structural layers & muted tones."
    elif temp < 75:
        outfit = "editorial_mid.jpg"
        msg = "Flowing linens & soft veranda blues."
    else:
        outfit = "editorial_hot.jpg"
        msg = "Minimalist silk & cupid pink accents."

    return jsonify({
        "temp": round(temp),
        "description": res['weather'][0]['description'],
        "suggestion": msg,
        "image": outfit
    })