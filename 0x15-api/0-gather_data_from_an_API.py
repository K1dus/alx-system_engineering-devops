#!/usr/bin/python3
'''Reads todo list from api for employee id passed'''

import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com/'


def do_request():
    '''Performs request'''
    if len(sys.argv) < 2:
        return print('USAGE:', __file__, '<employee id>')
    eid = sys.argv[1]
    try:
        _eid = int(sys.argv[1])
    except ValueError:
        return print('Employee id must be an integer')

    response = requests.get(base_url + 'users/' + eid)
    if response.status_code == 404:
        return print('User id not found')
    elif response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    user = response.json()

    response = requests.get(base_url + 'todos/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    todos = response.json()

    user_todos = [todo for todo in todos
                  if todo.get('userId') == user.get('id')]
    completed = [todo for todo in user_todos if todo.get('completed')]
    print('Employee', user.get('name'),
          'is done with tasks({}/{}):'.
          format(len(completed), len(user_todos)))
    [print('\t', todo.get('title')) for todo in completed]

if __name__ == '__main__':
    do_request()  
#!/usr/bin/python3

"""For a given employee ID, returns information about

their TODO list progress"""

import requests

import sys

if __name__ == "__main__":

    userId = sys.argv[1]

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"

                        .format(userId))

    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    totalTasks = 0

    completed = 0

    for task in todos.json():

        if task.get('userId') == int(userId):

            totalTasks += 1

            if task.get('completed'):

                completed += 1

    print('Employee {} is done with tasks({}/{}):'

          .format(name, completed, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()

          if task.get('userId') == int(userId) and task.get('completed')]))
