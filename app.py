from flask import Flask, render_template, request, jsonify
from model.recommender import recommend_destinations, generate_itinerary
import requests

app = Flask(__name__)

def get_weather(lat, lon):
    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current_weather=true"
        )
        return requests.get(url, timeout=5).json().get("current_weather", {})
    except:
        return None

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    itinerary = []
    weather = None

    if request.method == "POST":
        budget = int(request.form.get("budget"))
        days = int(request.form.get("days"))
        people = int(request.form.get("people"))
        interests = request.form.getlist("interests")
        region = request.form.get("region", "").strip().lower().replace("-", " ")

        visited_votes = {}
        visited_raw = request.form.get("visited_votes", "")
        for item in visited_raw.split(","):
            if ":" in item:
                place, votes = item.split(":")
                visited_votes[place.strip()] = int(votes.strip())

        df = recommend_destinations(interests, budget, days, visited_votes, people, region)

        if not df.empty:
            results = df.to_dict(orient="records")
            itinerary = generate_itinerary(results[0]["destination"], days, interests)
            weather = get_weather(results[0]["destination_latitude"], results[0]["destination_longitude"])

    return render_template("index.html", results=results, itinerary=itinerary, weather=weather)

@app.route("/update_itinerary")
def update_itinerary():
    dest = request.args.get('dest')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    days = int(request.args.get('days'))
    interests = request.args.getlist('interests')
    
    itinerary = generate_itinerary(dest, days, interests)
    weather = get_weather(lat, lon)
    
    return jsonify({
        "itinerary": itinerary,
        "weather": weather
    })

if __name__ == "__main__":
    app.run(debug=True)