#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


if __name__ == '__main__':
    """ fetching some data about user using third party api """

    prim_url = 'https://jsonplaceholder.typicode.com'
    name_endpoint = '/users/{}'
    tode_endpoint = '/todos?userId={}'

    # here we find the name of the user from /users/id endpoint
    name_res = requests.get(prim_url + name_endpoint.format(argv[1]))
    _dict1 = name_res.json()
    name = _dict1['name']

    # here we find the python object that represents the todos list
    todos_res = requests.get(prim_url + tode_endpoint.format(argv[1]))
    todos = todos_res.json()

    # let us count the completed task by user using the sum function
    completed_tasks = sum([1 for todo in todos if todo['completed']])

    # count the sum of the completed and non-completed taks
    total_completed_tasks = len(todos)

    print('Employee {} is done with tasks({}/{})'.format(
        name, completed_tasks, total_completed_tasks))

    # print the title of completed task
    for task in todos:
        if task['completed']:
            print('\t ', end='')
            print(task['title'])
