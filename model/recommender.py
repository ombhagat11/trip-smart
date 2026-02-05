import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# ================= LOAD DATA =================
# Get the absolute path to the CSV file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "data", "india_travel_destinations.csv")
df_master = pd.read_csv(CSV_PATH)

df_master["region"] = (
    df_master["region"].astype(str)
    .str.strip().str.lower().str.replace("-", " ")
)

# ================= FEATURE ENGINEERING =================
df_master["combined_features"] = (
    df_master["activities"].fillna("") + " " +
    df_master["travel_type"].fillna("")
)

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df_master["combined_features"])


# ================= RECOMMENDER =================
def recommend_destinations(interests, budget, days, visited_votes, people, region):

    df = df_master.copy()

    # Budget
    df = df[df["avg_daily_cost"] <= budget]
    if df.empty:
        return df

    # Region
    if region:
        df = df[df["region"] == region]
    if df.empty:
        return df

    # Group voting
    df["vote_penalty"] = 1.0
    for place, votes in visited_votes.items():
        place = place.lower()
        if votes >= (people // 2) + 1:
            df = df[df["destination"].str.lower() != place]
        else:
            df.loc[df["destination"].str.lower() == place, "vote_penalty"] = 0.6

    if df.empty:
        return df

    # Interest similarity
    user_text = " ".join(interests)
    user_vector = tfidf.transform([user_text])

    similarity = cosine_similarity(
        user_vector,
        tfidf.transform(df["combined_features"])
    )[0]

    df["interest_score"] = similarity
    df["duration_score"] = (
        1 - abs(df["recommended_days"] - days) / df["recommended_days"]
    ).clip(0, 1)
    df["rating_score"] = df["rating"] / 5

    # Final weighted score
    df["final_score"] = (
        0.45 * df["interest_score"] +
        0.25 * df["duration_score"] +
        0.20 * df["rating_score"]
    ) * df["vote_penalty"]

    # Normalize for UI
    df["final_score_pct"] = (
        (df["final_score"] / df["final_score"].max()) * 100
    ).round(1)

    # ================= EXPLAINABILITY =================
    def interest_label(x):
        if x > 0.7: return "Strong interest match"
        if x > 0.4: return "Moderate interest match"
        return "Low interest match"

    def duration_label(x):
        if x > 0.8: return "Ideal trip length"
        if x > 0.5: return "Acceptable duration"
        return "May feel rushed or long"

    def rating_label(x):
        if x > 0.85: return "Top-rated destination"
        if x > 0.7: return "Well-reviewed destination"
        return "Average traveler ratings"

    df["why_interest"] = df["interest_score"].apply(interest_label)
    df["why_duration"] = df["duration_score"].apply(duration_label)
    df["why_rating"] = df["rating_score"].apply(rating_label)
    df["group_acceptance"] = (df["vote_penalty"] * 100).round(0)

    return df.sort_values("final_score", ascending=False).head(5)


# ================= PERSONALIZED ITINERARY =================
def generate_itinerary(destination, days, interests):

    activity_pool = {
        "Adventure": ["trekking", "river rafting", "sunrise hike"],
        "Nature": ["nature walk", "waterfall visit", "scenic viewpoint"],
        "Beach": ["beach leisure", "sunset walk", "water sports"],
        "Cultural": ["heritage walk", "museum visit", "local markets"],
        "Relaxation": ["spa session", "café hopping", "free exploration"]
    }

    activities = []
    for i in interests:
        activities.extend(activity_pool.get(i, []))
    if not activities:
        activities = ["local sightseeing", "leisure exploration"]

    itinerary, idx = [], 0
    for day in range(1, days + 1):
        plan = []
        if day == 1:
            plan += [f"Arrival at {destination}", "Hotel check-in"]

        plan.append(activities[idx % len(activities)])
        idx += 1
        plan.append(activities[idx % len(activities)])
        idx += 1

        if day == days:
            plan.append("Shopping and departure")

        itinerary.append(f"Day {day}: " + ", ".join(plan))

    return itinerary
