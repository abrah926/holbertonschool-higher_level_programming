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
            print(f"Title: {post.title")
