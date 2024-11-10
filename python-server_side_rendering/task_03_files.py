import json
import csv
import os
from flask import Flask, render_template, request, abort

app = Flask(__name__)

json_file_path = os.path.join(os.path.dirname(__file__), 'products.json')
csv_file_path = os.path.join(os.path.dirname(__file__), 'products.csv')

# Function to read data from JSON file


def read_json_data():
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None


def read_csv_data():
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            products = []
            for row in reader:
                row['id'] = int(row['id'])  # Ensure type conversion
                row['price'] = float(row['price'])
                products.append(row)
            return products
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
    product_id = request.args.get('product_id')

    products_data = []

    if source == 'json':
        products_data = read_json_data()
        if not products_data:
            return render_template('product_display.html', error="JSON file not found or is empty.")
    elif source == 'csv':
        products_data = read_csv_data()
        if not products_data:
            return render_template('product_display.html', error="CSV file not found or is empty.")
    else:
        return render_template('product_display.html', error="Invalid source parameter. Please use json or csv.")

    if product_id:
        products_data = [product for product in products_data if str(
            product.get('id')) == product_id]
        if not products_data:
            return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
