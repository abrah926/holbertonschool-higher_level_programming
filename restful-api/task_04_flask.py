#!/usr/bin/python3
"""Simple API using Python with Flask"""


from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def json_data():
    if not users:
        return jsonify({"error": "User not found"}), 200
    usernames = list(users.keys())
    return jsonify(usernames), 200


@app.route("/status")
def status():
    return ("OK")


# Dynamic route feature in flask
@app.route("/users/<username>")
def get_users(username):
    user = users.get(username)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    username = data.get('username')
    name = data.get('name')
    age = data.get('age')
    city = data.get('city')

    if not all([username, name, age, city]):
        return jsonify({"error": "Missing data"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = {"name": name, "age": age, "city": city}
    users.append(users)

    return jsonify({"message": "User added successfully", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
