#!/usr/bin/python3
""" Module to gather data from an API """
import csv
import requests
from sys import argv


def save_tasks_to_csv(employeeId):
    """ save data to csv """
    username = ''
    allTasks = []

    usersRes = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(employeeId))
    todosRes = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos"
            .format(employeeId))

    username = usersRes.json().get('username')
    todosJson = todosRes.json()

    for task in todosJson:
        taskRow = []
        taskRow.append(employeeId)
        taskRow.append(username)
        taskRow.append(task.get('completed'))
        taskRow.append(task.get('title'))
        allTasks.append(taskRow)

    with open("{}.csv".format(employeeId), 'w') as csvFile:
        csvwriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(allTasks)
    return 0

if __name__ == '__main__':
    save_tasks_to_csv(argv[1])
