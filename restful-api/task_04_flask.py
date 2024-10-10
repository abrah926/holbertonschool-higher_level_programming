from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def get_usernames():
    return jsonify(list(users.keys()))


@app.route('/status', methods=['GET'])
def status():
    return "OK"


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 409

    users[username] = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run(debug=True)