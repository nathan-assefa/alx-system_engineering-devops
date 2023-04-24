#!/usr/bin/python3
""" This script talks to jsonplaceholder api to fetch
data about a user that includes the name of the user from
/users api endpoint and todo lists from todos?userId={} api
endpoint """


import requests
import sys


if __name__ == __main__:
    """ talking to jsonplaceholder api """
    # The base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # The endpoint for retrieving employee information
    employee_endpoint = '/users/{}'

    # The endpoint for retrieving TODO list information
    todo_endpoint = '/todos?userId={}'

    # The employee ID is provided as a command line argument
    employee_id = sys.argv[1]

    # Retrieve employee information
    employee_response = requests.get(base_url + employee_endpoint.format(employee_id))
    employee = employee_response.json()

    # Retrieve TODO list information
    todo_response = requests.get(base_url + todo_endpoint.format(employee_id))
    todos = todo_response.json()

    # Count the number of completed and total tasks
    num_completed_tasks = sum([1 for todo in todos if todo['completed']])
    num_total_tasks = len(todos)

    # Display the employee's TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(employee['name'], num_completed_tasks, num_total_tasks))
    for todo in todos:
        if todo['completed']:
            print("\t {} {}".format('\t', todo['title']))
