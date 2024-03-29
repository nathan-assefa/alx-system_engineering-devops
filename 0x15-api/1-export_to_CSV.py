#!/usr/bin/python3

"""
This script talks to jsonplaceholder api to fetch
data about a user that includes the name of the user from
/users api endpoint and todo lists from todos?userId={} api
endpoint
"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # find the user name from the 'users' end point, and parse it
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    user_name = user.get("username")
    user_id = user.get("id")

    # find the list of todos and parse it into python list
    todos = requests.get(url + "todos?userId={}".format(sys.argv[1])).json()

    # let define the name of the file
    file_name = "{}.csv".format(sys.argv[1])

    # let us create and open the file as csv file
    with open(file_name, "w") as csvfile:
        # let us create the 'writer' object that helps us to wrap our
        # file with csv library functionality
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow(
                [user_id, user_name, task.get("completed"), task.get("title")]
            )
