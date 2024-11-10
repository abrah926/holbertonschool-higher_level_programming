import json
import os
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    json_file_path = os.path.join(os.path.dirname(__file__), 'items.json')
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecoderError):
        items_list = []
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
