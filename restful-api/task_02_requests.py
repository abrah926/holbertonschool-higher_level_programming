#!/usr/bin/env python


import requests
import json
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status code: " {response.status_code})

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    if response.status_code == 200:
        post = response.json()

        structured_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        with open('post.csv', 'w', newline='') as csv_file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_data)

    print("Post saved to post.csv")
