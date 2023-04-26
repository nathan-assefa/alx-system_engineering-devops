#!/usr/bin/python3
import requests
import sys
import json


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = response.json()
    todo_data = {}
    for user in users:
        url = f"https://jsonplaceholder.typicode.com/users/{user['id']}/todos"
        response = requests.get(url)
        tasks = response.json()
        todo_data[user['id']] = []
        for task in tasks:
            task_dict = {
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed']
            }
            todo_data[user['id']].append(task_dict)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(todo_data, f)
