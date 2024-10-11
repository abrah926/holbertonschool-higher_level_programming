from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/clear_users')
def clear_users():
    global users
    users.clear()
    return jsonify({"message": "All users cleared"}), 200


@app.route('/data')
def data():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.get_json()
    if not new_user or 'username' not in new_user:
        return jsonify({"error": "Username is required"}), 400

    username = new_user['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 409

    users[username] = new_user
    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201


if __name__ == '__main__':
    app.run(debug=True)
