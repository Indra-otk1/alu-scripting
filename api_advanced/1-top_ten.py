#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:api_advanced.top_ten:v1.0"}

    response = requests.get(
        url,
        headers=headers,
        params={"limit": 10},
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data")
    if not data or "children" not in data:
        print(None)
        return

    for post in data["children"][:10]:
        print(post["data"]["title"])