#!/usr/bin/python3
""" return list contaning the title of hot articles
for a given subreddit """
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """ reuturns all hot articles"""
    endpoint = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16-api_advanced.0-sub.py:\
        v1.0.0 (by /u/thomaskitaba)"
    }
    params = {
            "limit": 100,
            "after": after,
            "count": count
            }
    response = requests.get(endpoint, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 404:
        return None

    data = response.json().get("data")
    children = data.get("children")
    after = data.get("after")
    count += int(data.get("dist"))
    for post in children:
        hot_list.append(post.get("data").get("title"))

    if after is not None:
        recurse(subreddit, hot_list, after, count)
    return hot_list
