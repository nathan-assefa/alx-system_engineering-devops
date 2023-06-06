#!/usr/bin/python3
"""
    Writing a function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "MyRedditScript/1.0 (Linux; Python)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]

            # Print the titles of the first 10 hot posts
            for post in posts[:10]:
                title = post["data"]["title"]
                print(title)
        else:
            print("None")
    except requests.RequestException:
        print("None")
