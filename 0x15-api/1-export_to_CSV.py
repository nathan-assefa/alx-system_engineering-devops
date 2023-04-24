#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
"""


import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"
            ])
        for todo in todos:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": str(todo["completed"]),
                "TASK_TITLE": todo["title"]
            })
