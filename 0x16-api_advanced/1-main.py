#!/usr/bin/python3
""" display top 10 posts for a given subredit """
import requests

if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search")
    else:
        top_ten(sys.argv[1])
