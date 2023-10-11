#!/usr/bin/python3
"""Finds the number of subscribers in a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """ call redit api """
    endpoint = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16-api_advanced.0-sub.py:\
        v1.0.0 (by /u/thomaskitaba)"
    }
    response = requests.get(endpoint, headers=headers,
                            allow_redirects=False)
    # print(response)

    if response.status_code == 404:
        return 0
    data = response.json().get("data")
    subscribers = data.get("subscribers")
    return subscribers
