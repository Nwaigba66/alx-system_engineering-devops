#!/usr/bin/python3
""" display top 10 posts for a given subredit """
import requests


def top_ten(subreddit):
    """ call redit api """
    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers =:\
        v1.0.0 (by /u/Nwaigba66)"
    }
    response = requests.get(endpoint, headers=headers,
                            allow_redirects=False, params={"limit": 10})
    # print(response)
    if response.status_code == 404:
        print("None")
        return
    data = response.json().get("data").get("children")
    for post in data:
        print(post.get("data").get("title"))
