#!/usr/bin/python3
""" Writing a recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit  """


import requests


def recurse(subreddit, hot_list=None, after=None):
    """ Recursive funtion that queries the Reddit API """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditScript/1.0 (Linux; Python)"}
    params = {"after": after, "limit": 100} if after else {"limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            after = data["data"]["after"]

            for post in posts:
                title = post["data"]["title"]
                hot_list.append(title)

            if after:
                return recurse(subreddit, hot_list, after=after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
