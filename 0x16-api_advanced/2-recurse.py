#!/usr/bin/bash
""" Writing a recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit  """


import requests


def recurse(subreddit, hot_list=[], after=None):
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    HEADERS = {'User-Agent': 'Unix:0-subs:v1'}
    params = {'limit': 100}

    if after and after != "STOP":
        params['after'] = after

    response = requests.get(URL, headers=HEADERS, params=params)
    data = response.json().get('data', {})

    if response.status_code != 200 or not data:
        return None

    after = data.get('after', 'STOP')
    posts = data.get('children', [])

    hot_list += [post.get('data', {}).get('title') for post in posts]

    if not after:
        after = "STOP"

    if after == "STOP":
        return hot_list[:10]

    return recurse(subreddit, hot_list, after)
