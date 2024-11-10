#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

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
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items = data['items']
            return render_template('items.html', items=items)
    except Exception as e:
        return render_template('items.html', items=[])


def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []


def read_csv_file(filename):
    try:
        with open(filename, newline='') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        return []


@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Handle invalid source
    if source not in ['json', 'csv']:
        # Return 400 status code
        return render_template('product_display.html', error="Wrong source. Please use json or csv."), 400

    # Read products based on source
    if source == 'json':
        products = read_json_file('products.json')

    elif source == 'csv':
        products = read_csv_file('products.csv')

    # Handle missing products
    if not products:
        return render_template('product_display.html', error="No products found.")

    # If product_id is provided, filter the products
    if product_id:
        products = [product for product in products if str(
            product['id']) == str(product_id)]
        if not products:
            return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
