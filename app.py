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
    if temp < 0:
        outfit = "lo.png"
        msg = "Grab a vibrant parka to brighten your cold day!"
    elif temp < 32:
        outfit = "midlo.png"
        msg = "Settle into your cozy vibe with some dark colors :)"
    elif temp < 50:
        outfit = "mid.png"
        msg = "Pair a pastel cardigan with some cute pants!"
    elif temp < 68:
        outfit = "midhi.png"
        msg = "Throw on some gingham or overalls to embrace the nice day! "
    elif temp < 80:
        outfit = "hi.png"
        msg = "Put on some shorts and beachy colors for this hot day :)"
    else:
        outfit = "hihi.png"
        msg = "Wear some athletic clothes and soak up the sun!"

    return jsonify({
        "temp": round(temp),
        "description": res['weather'][0]['description'],
        "suggestion": msg,
        "image": outfit
    })