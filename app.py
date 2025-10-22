
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<h1>EarnToWatch Backend is Running</h1>"

@app.route("/api/referral-leaderboard", methods=["GET"])
def referral_leaderboard():
    leaderboard = [
        {"user_id": "user123", "referrals": 12},
        {"user_id": "user456", "referrals": 9},
        {"user_id": "user789", "referrals": 5}
    ]
    return jsonify(leaderboard)

@app.route("/api/request-cashout", methods=["POST"])
def request_cashout():
    data = request.get_json()
    user_id = data.get("user_id")
    amount = data.get("amount")
    timestamp = data.get("timestamp")

    if not user_id or not amount:
        return jsonify({"success": False, "message": "Missing user_id or amount"}), 400

    # Simulate success response
    return jsonify({"success": True, "message": "Cashout request submitted", "new_balance": 0})

if __name__ == "__main__":
    app.run(debug=True)
