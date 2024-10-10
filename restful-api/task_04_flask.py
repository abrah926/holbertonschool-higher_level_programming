from flask import Flask, jsonify

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 32, "city": "New York"},
}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/status', methods=['GET'])
def status():
    return 'OK'


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
    username = data.get('username')
    if username in users:
        return jsonify({'error': 'User already exists'}), 400
    users[username] = {'name': data.get('name'), 'age': data.get(
        'age'), 'city': data.get('city')}
    return jsonify({'message': 'User added successfully', 'user': users[username]}), 201


if __name__ == "__main__":
    app.run(port=5000)
