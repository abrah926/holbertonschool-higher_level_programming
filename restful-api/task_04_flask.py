#!/usr/bin/python3
"""
This script starts a Flask API server.
"""


from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """
    Home route of the API.

    Returns:
        str: Welcome message for home route.
    """
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    """
    Status route of the API.

    Returns:
        str: Status OK message.
    """
    return "OK"


@app.route('/data')
def data():
    """
    Data route of the API.

    Returns:
        Response: JSON response containing a list of usernames.
    """
    return jsonify(list(users.keys()))


@app.route('/users/<username>')
def get_user(username):
    """
    Get a specific user by username.

    Args:
        username (str): The username to look up.

    Returns:
        Response: JSON response containing user data or error message.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add a new user.

    Returns:
        Response: JSON response confirming user added or error message.
    """
    new_user = request.get_json()
    username = new_user.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    users[username] = new_user
    print(f"Added user: {username}")
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run(debug=True)
