#!/usr/bin/python3
""" Module to gather data from an API """
import json
import requests
from sys import argv


def save_to_json(employeeId):
    """for api"""
    username = ''
    userDict = {}

    usersRes = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".
        format(employeeId))
    todosRes = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".
        format(employeeId))

    username = usersRes.json().get('username')
    todosJson = todosRes.json()

    userDict[employeeId] = []

    for task in todosJson:
        taskDict = {}
        taskDict['task'] = task.get('title')
        taskDict['username'] = username
        taskDict['completed'] = task.get('completed')

        userDict[employeeId].append(taskDict)

    with open("{}.json".format(employeeId), 'w') as jFile:
        json.dump(userDict, jFile)

if __name__ == '__main__':
    save_to_json(argv[1])
