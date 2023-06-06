#!/usr/bin/python3
""" Writing a recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit  """


import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Recursive funtion that queries the Reddit API """

    url = "https://www.reddit.com/r/{}/hot.json".format('subreddit')
    headers = {'User-Agent': 'MyRedditScript/1.0 (Linux; Python)'}
    params = {"limit": 100, "after": after} if after else {"limit": 100}

    try:
        response = requests.get(
                url, headers=headers, params=params, allow_redirects=False
                )
        data = response.json()

        if response.status_code == 200:
            posts = data.get("data", {}).get("children", [])
            for post in posts:
                title = post.get("data", {}).get("title")
                hot_list.append(title)

            after = data.get("data", {}).get("after")
            if after:
                return recurse(subreddit, hot_list, after=after)
            else:
                return hot_list
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None