#!/usr/bin/python3
"""
    Writing a function that queries the Reddit API and returns
    the number of subscribers
"""


import requests


def number_of_subscribers(subreddit):
    """ Returning the number of subscribers from Reddit API """

    # First, we make a request for the specific subreddit
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Then, we compose the User-Agent header
    headers = {"User-Agent": "MyRedditScript/1.0 (Linux; Python)"}

    try:
        # Make the HTTP request to the Reddit server
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            no_of_subscribers = response.json()["data"]["subscribers"]
            return no_of_subscribers

        # Return 0 if the subreddit is not valid or an error occurred
        return 0

    except requests.RequestException:
        return 0
