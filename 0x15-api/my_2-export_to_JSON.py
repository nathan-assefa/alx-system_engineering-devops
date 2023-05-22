#!/usr/bin/python3

"""
This script talks to jsonplaceholder api to fetch
data about a user that includes the name of the user from
/users api endpoint and todo lists from todos?userId={} api
endpoint
"""


import requests
import csv
from sys import argv
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # find the user name from the 'users' end point, and parse it
    user = requests.get(url + "users/{}".format(argv[1])).json()
    user_name = user.get("username")
    user_id = user.get("id")

    # find the list of todos and parse it into python list
    todos = requests.get(url + "todos?userId={}".format(argv[1])).json()

    # let define the name of the file
    file_name = "{}.json".format(argv[1])

    emp_data = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user_name,
            }
            for task in todos
        ]
    }
    with open(file_name, 'w') as jsonfile:
        json.dump(emp_data, jsonfile)
