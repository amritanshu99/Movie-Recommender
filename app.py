# app.py
from flask import Flask, request, jsonify
from recommender import recommend_movies

app = Flask(__name__)

@app.route("/")
def home():
    return "🎬 Movie Recommender API is running!"



@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    movie = data.get("movie")
    top_n = int(data.get("top_n", 5))

    if not movie:
        return jsonify({"error": "Movie title required"}), 400

    recommendations = recommend_movies(movie, top_n)
    return jsonify({
        "input": movie,
        "recommendations": recommendations
    })

if __name__ == "__main__":
    app.run(debug=True)
