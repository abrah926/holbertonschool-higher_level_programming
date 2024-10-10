from flask import Flask, jsonify


app = Flask(__name__)

users = {

    'jane': {'name': 'Jane', 'age': 28, 'city': 'Los Angeles'},
    john: {'name': 'John', 'age': 32, 'city': 'New York'},
}


@app.route('/')
def home():
    return 'Welcome to Flask API!'


@app.route('/data', methods=['GET'])
def get_users():
    return jsonify(users)


if __name__ == '__main__':
    app.run(port=5000)
