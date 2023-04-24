#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open(f"{user_id}.csv", "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    for todo in todos:
        writer.writerow(
            {
                "USER_ID": todo["userId"],
                "USERNAME": "",  # Add the employee username here
                "TASK_COMPLETED_STATUS": str(todo["completed"]),
                "TASK_TITLE": todo["title"],
            }
        )
