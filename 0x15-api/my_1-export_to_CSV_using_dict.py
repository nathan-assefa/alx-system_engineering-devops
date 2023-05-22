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


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # find the user name from the 'users' end point, and parse it
    user = requests.get(url + "users/{}".format(argv[1])).json()
    user_name = user.get('username')
    user_id = user.get('id')

    # find the list of todos and parse it into python list
    todos = requests.get(url + "todos?userId={}".format(argv[1])).json()


    # let define the name of the file
    file_name = '{}.csv'.format(argv[1])

    fieldnames = ['user_id', 'user_name', 'tasks_status', 'title']

    # let us create and open the file as csv file
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        writer.writeheader()

        for task in todos:
            writer.writerow({
                'user_id': user_id,
                'user_name': user_name,
                'tasks_status': task.get('completed'),
                'title': task.get('title')
                }
                )
