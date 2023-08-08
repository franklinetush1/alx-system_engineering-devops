#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests

def recurse(subreddit, hot_list=[]):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return None
    
    data = response.json()["data"]
    hot_list.extend([post["data"]["title"] for post in data["children"]])

    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list)
    else:
        return hot_list
