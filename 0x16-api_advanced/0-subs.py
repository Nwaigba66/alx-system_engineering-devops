#!/usr/bin/python3
""" A function that finds the number of subscribers
"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """Finds the number of subscribers in a subreddit

    Return: integer number of subscribers if found else 0
    """
    url = 'https://www.reddit.com/r/{}/about.json'
    request = requests.get(
            url.format(subreddit),
            headers={'User-Agent': 'Gloria'},
            allow_redirects=False)
    try:
        data = json.loads(req.text)
        return (data['data']['subscribers'])
    except Exception as e:
        return 0
