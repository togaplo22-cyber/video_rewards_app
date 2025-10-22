
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Sample leaderboard data
leaderboard = [
    {"user_id": "user123", "referrals": 15},
    {"user_id": "user456", "referrals": 10},
    {"user_id": "user789", "referrals": 7}
]

@app.route("/api/referral-leaderboard", methods=["GET"])
def get_leaderboard():
    sorted_board = sorted(leaderboard, key=lambda x: x["referrals"], reverse=True)
    return jsonify(sorted_board)

@app.route("/api/request-cashout", methods=["POST"])
def request_cashout():
    data = request.get_json()
    user_id = data.get("user_id")
    amount = data.get("amount")
    timestamp = data.get("timestamp")

    if amount < 100:
        return jsonify({"success": False, "message": "Minimum cashout is ₱100"})

    return jsonify({"success": True, "message": "Cashout request accepted", "user_id": user_id, "amount": amount})

if __name__ == "__main__":
    app.run(debug=True)
