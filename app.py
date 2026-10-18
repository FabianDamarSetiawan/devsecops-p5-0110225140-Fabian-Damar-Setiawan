from flask import Flask, jsonify, request
from services import UserService

app = Flask(__name__)
user_service = UserService()

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "running", "message": "DevSecOps Pipeline App Active"})

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)