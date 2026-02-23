#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts for a given subreddit.
"""
from requests import get


def top_ten(subreddit):
    """Query Reddit API and print titles of first 10 hot posts."""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    user_agent = {'User-agent': 'python:holberton.top_ten:v1.0'}
    params = {'limit': 10}

    response = get(url, headers=user_agent, params=params,
                   allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        results = response.json()
        my_data = results.get('data').get('children')
        for i in my_data:
            print(i.get('data').get('title'))
    except Exception:
        print(None)