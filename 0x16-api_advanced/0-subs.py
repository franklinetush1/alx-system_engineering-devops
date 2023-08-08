#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    headers = {"User-Agent":
               "linux:0x16.api.advanced:v1.0.0 (by franklinetush1@gmail.com)"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        return data.get("subscribers")
    else:
        return 0
