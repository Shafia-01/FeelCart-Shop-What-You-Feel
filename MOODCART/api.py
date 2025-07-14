from flask import Flask, request, jsonify
import json
from moodcart_model import predict_mood_category

app = Flask(__name__)

# Load mood history from file
with open("MOODCART/mood_history.json", "r") as f:
    mood_data = json.load(f)

@app.route("/moodcart", methods=["POST"])
def moodcart():
    data = request.get_json()
    mood = data.get("mood")

    if not mood:
        return jsonify({"error": "Missing mood"}), 400

    # You can extend this to use mood history if needed
    emotion, category, confidence = predict_mood_category(mood)
    return jsonify({
        "emotion": emotion,
        "category": category,
        "confidence": confidence
    })


if __name__ == "__main__":
    app.run(debug=True)

