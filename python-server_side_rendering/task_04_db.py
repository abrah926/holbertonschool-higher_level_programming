#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

    if source == 'json':
        products = read_json_file('products.json')

    elif source == 'csv':
        products = read_csv_file('products.csv')

    elif source == 'sql':
        products = read_sqlite_data()

    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        products = [product for product in products if str(
            product['id']) == str(product_id)]
        if not products:
            return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)


def read_sqlite_data():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        products = cursor.fetchall()
        conn.close()

        product_list = []
        for product in products:
            product_list.append({
                'id': product[0],
                'name': product[1],
                'category': product[2],
                'price': product[3]
            })
        return product_list
    except sqlite3.Error as e:
        print(f'Database error: {e}')
        return []


if __name__ == '__main__':
    app.run(debug=True, port=5000)
