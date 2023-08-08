#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    headers = {"User-Agent":
               "linux:0x16.api.advanced:v1.0.0 (by franklinetush1@gmail.com)"}
    parameters = {"limit": 10}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    response = requests.get(url, headers=headers, params=parameters,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        [print(item.get("data").get("title")) for item in data.get("children")]
    else:
        print("None")
        return
