import json
import csv
import os
from flask import Flask, render_template, request, abort

app = Flask(__name__)

json_file_path = os.path.join(os.path.dirname(__file__), 'products.json')
csv_file_path = os.path.join(os.path.dirname(__file__), 'products.csv')


def read_json_data():
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('products', [])
    except FileNotFoundError:
        return None


def read_csv_data():
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return None


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


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    products_data = []
    error_message = None

    if source == 'json':
        products_data = read_json_data()
        if products_data is None:
            error_message = "JSON file not found."

    elif source == 'csv':
        products_data = read_csv_data()
        if products_data is None:
            error_message = "CSV file not found."

    else:
        error_message = "Wrong source. Please use 'json' or 'csv'."

    if not error_message and product_id:
        filtered_data = [
            product for product in products_data if product.get('id') == product_id]
        if filtered_data:
            products_data = filtered_data
        else:
            error_message = "Product not found."

    return render_template('product_display.html', products=products_data, error=error_message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
