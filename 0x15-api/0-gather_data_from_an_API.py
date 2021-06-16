#!/usr/bin/python3
# Gather data from an API
import requests
import sys

def get_employee_tasks(employeeID):
    name = ' '
    taskList = []
    completed_counter = 0

    usersRes = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(employeeID))
    todosRes = requests.get('https://jsonplaceholder.typicode.com/users/{}/\
                            todos'.format(employeeID))

    name = usersRes.json().get('name')
    print('Name: {}'.format(name))

    todosJson = todosRes.json()

    for task in todosJson:
        if task.get('completed') is True:
            completed_counter += 1
            taskList.append(task.get('title'))
    print('task_list: {}'.format(taskList))
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed_counter, len(todosJson)))
    for title in taskList:
        print('\t {}'.format(title))
    return 0

if __name__== "__main__":
    get_employee_tasks(sys.argv[1])
