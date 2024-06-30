#!/usr/bin/python3
"""Module to get the number of subscribers for a subreddit."""

import json
import requests
import sys


def number_of_subscribers(subreddit):
    """Function that returns the number of subscribers from the Reddit API."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyRedditBot/1.0 (by YourUsername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Handle redirects which indicate invalid subreddits
        if response.status_code == 301 or response.status_code == 302:
            return 0
        if response.status_code == 200:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
        else:
            return 0
    except requests.RequestException:
        return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        num_subscribers = number_of_subscribers(subreddit)
        print(num_subscribers)
