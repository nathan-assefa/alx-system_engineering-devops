#!/usr/bin/python3

"""
This script talks to jsonplaceholder api to fetch
data about a user that includes the name of the user from
/users api endpoint and todo lists from todos?userId={} api
endpoint
"""


import requests
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # find the user name from the 'users' end point, and parse it
    users = requests.get(url + "users").json()

    # find the list of todos and parse it into python list
    todos = requests.get(url + "todos?").json()

    emp_data = {
            user.get('id'): [
                {
                    "username": user.get('username'),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                    }
                for task in todos
        ] for user in users
    }
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(emp_data, jsonfile)
