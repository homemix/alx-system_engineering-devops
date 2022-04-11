#!/usr/bin/python3
""" Dictionary of list of dictionaries
 Records all tasks from all employees """
import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    r = requests.get(url)
    user = r.json()
    url = 'https://jsonplaceholder.typicode.com/todos'
    r = requests.get(url)
    todo = r.json()
    data = {}
    for user in todo:
        if user['userId'] not in data:
            data[user['userId']] = []
        data[user['userId']].append({
            'task': user['title'],
            'completed': user['completed']
        })
    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)
    f.close()
    print('File saved!')

