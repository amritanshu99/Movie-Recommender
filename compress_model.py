# compress_model.py

import pickle
import joblib

# Load the original .pkl (created with pickle)
with open("recommender.pkl", "rb") as f:
    df, cosine_sim, indices = pickle.load(f)

# Save compressed version with joblib (compression level 3–5 is ideal)
joblib.dump((df, cosine_sim, indices), "recommender_compressed.pkl", compress=3)

print("✅ Model compressed and saved as 'recommender_compressed.pkl'")
