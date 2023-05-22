#!/usr/bin/python3

"""
This script talks to jsonplaceholder api to fetch
data about a user that includes the name of the user from
/users api endpoint and todo lists from todos?userId={} api
endpoint
"""


import requests
from sys import argv


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    
    # find the user name from the 'users' end point, and parse it 
    user = requests.get(url + 'users/{}'.format(argv[1])).json()
    user_name = user['name']
    # Notice: the json() method is part of the response object

    # find the list of todos and parse it into python list
    todos = requests.get(url + 'todos?userId={}'.format(argv[1])).json()

    # find number of tasks done by the user
    tasks_done = [task_done for task_done in todos if task_done['completed']]

    len_tasks_done = len(tasks_done)

    # total number of tasks

    total_task = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        user_name, len_tasks_done, total_task
        ))
 
    # printing each completed tasks using list comperehesion
    [print('\t {}'.format(task.get('title'))) for task in tasks_done]
    
