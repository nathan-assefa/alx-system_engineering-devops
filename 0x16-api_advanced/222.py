#!/usr/bin/python3
""" Writing a recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit  """


import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"after": after, "limit": 100} if after else {"limit": 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    for data in results.get("children"):
        hot_list.append(data.get("data").get("title"))

    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list

""" The after parameter is used to indicate to the Reddit API which specific
page of results you want to retrieve. It acts as a marker or reference point
for the API to know from where to continue fetching the next set of results.

Initially, when you make the first request to the API, you don't have an
after value because you haven't fetched any pages yet. The API will respond
with the first set of results along with an after value. This after value
corresponds to the last item of the current page of results.

In subsequent recursive calls, you include the after value as a parameter to
the recurse() function. This allows you to pass the after value from the
previous response to the next API request. By including the after value in
the request parameters, you're telling the API to retrieve the next page of
results starting from that particular item.

So, in each recursive call, the after value is passed as a 
parameter to the function """
