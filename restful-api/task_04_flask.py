#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    if "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data["username"]

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "username": username,
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
