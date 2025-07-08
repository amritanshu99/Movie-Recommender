# compress_pickle.py

import pickle
import joblib

# 🔁 Load original recommender.pkl
with open("recommender.pkl", "rb") as f:
    df, cosine_sim, indices = pickle.load(f)

# 💾 Save compressed version using joblib
joblib.dump((df, cosine_sim, indices), "recommender_compressed.pkl", compress=3)

print("✅ Compression done! Saved as 'recommender_compressed.pkl'")
