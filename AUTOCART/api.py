from flask import Flask, request, jsonify
import json
from autocart_engine import generate_autocart

app = Flask(__name__)

# Load user history from file
with open("AUTOCART/user_history.json", "r") as f:
    user_data = json.load(f)

@app.route("/autocart", methods=["POST"])
def autocart():
    data = request.get_json()
    user_id = data.get("user_id")

    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    user_history = user_data.get(user_id)

    if not user_history:
        return jsonify({"error": f"No data found for user_id: {user_id}"}), 404

    recommendations = generate_autocart(user_history)
    return jsonify({"user_id": user_id, "recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
