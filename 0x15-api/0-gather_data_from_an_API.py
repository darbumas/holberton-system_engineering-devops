#!/usr/bin/python3
""" Module to gather data from an API """
import requests
from sys import argv


def get_employee_tasks(employeeId):
    """ Gather data """
    name = ''
    task_list = []
    idx = 0

    usersRes = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employeeId))
    todosRes = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".
        format(employeeId))

    name = usersRes.json().get('name')
    todosJson = todosRes.json()

    for task in todosJson:
        if task.get('completed') is True:
            idx += 1
            task_list.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(
        name, idx, len(todosJson)))
    for title in task_list:
        print('\t {}'.format(title))
    return 0

if __name__ == '__main__':
    get_employee_tasks(argv[1])
