# recommender.py
import joblib
from rapidfuzz import process

# 1️⃣ Load compressed model from repo (must be < 100MB to avoid GitHub issues)
print("📦 Loading recommender model...")
df, cosine_sim, indices = joblib.load("recommender.pkl")
print("✅ Model loaded successfully!")

# 2️⃣ Match closest movie title using fuzzy match
def get_closest_title(input_title, all_titles):
    match = process.extractOne(input_title, all_titles, score_cutoff=60)
    if match:
        return match[0]
    return None

# 3️⃣ Recommend similar movies
def recommend_movies(input_title, num=5):
    actual_title = get_closest_title(input_title, df["title"])
    if not actual_title:
        return [f"❌ Movie not found: '{input_title}'"]

    idx = indices[actual_title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num+1]
    movie_indices = [i[0] for i in sim_scores]

    print(f"🎬 Interpreted '{input_title}' as '{actual_title}'")
    return df["title"].iloc[movie_indices].tolist()
