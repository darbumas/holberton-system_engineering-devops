#!/usr/bin/python3
"""Module to gather data from an API"""
import json
import requests
from sys import argv


def export_all_to_json():
    """ export data in the JSON format """
    users_and_tasks = {}

    users_json = requests.get("https://jsonplaceholder.typicode.com/users/")\
        .json()
    todos_json = requests.get("https://jsonplaceholder.typicode.com/todos")\
        .json()

    user_info = {}
    for user in users_json:
        user_info[user['id']] = user['username']

    for task in todos_json:
        if users_and_tasks.get(task['userId'], False) is False:
            users_and_tasks[task['userId']] = []
        task_dict = {}
        task_dict['username'] = user_info[task['userId']]
        task_dict['task'] = task['title']
        task_dict['completed'] = task['completed']
        users_and_tasks[task['userId']].append(task_dict)

    with open("todo_all_employees.json", 'w') as jFile:
        json.dump(users_and_tasks, jFile)

if __name__ == '__main__':
    export_all_to_json()
