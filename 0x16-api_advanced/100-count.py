#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""

import requests


def count_words(subreddit, word_list):
    """Prints counts of given words"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent":
               "linux:0x16.api.advanced:v1.0.0 (by franklinetush1@gmail.com)"}
    params = {"limit": 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    try:
        results = response.json()["data"]
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    instances = {}
    after = results.get("after")
    count = results.get("dist")
    for c in results.get("children"):
        title = c["data"]["title"].lower().split()
        for word in word_list:
            times = title.count(word.lower())
            instances[word] = instances.get(word, 0) + times

    if after is None:
        if not instances:
            print("")
            return
        sorted_instances = sorted(instances.items(),
                                  key=lambda kv: (-kv[1], kv[0]))
        for k, v in sorted_instances:
            print(f"{k}: {v}")
    else:
        count_words(subreddit, word_list)
