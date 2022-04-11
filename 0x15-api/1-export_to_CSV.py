#!/usr/bin/python3
""" Export data in the APi database to a CSV file """
import requests
import csv
import sys

user_id = sys.argv[1]
if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}' \
        .format(user_id)
    r = requests.get(url)
    r_json = r.json()
    url = 'https://jsonplaceholder.typicode.com/users/{}' \
        .format(user_id)
    r = requests.get(url)
    r_json_user = r.json()
    user_name = r_json_user.get('username')

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in r_json:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': user_name,
                'TASK_COMPLETED_STATUS': task.get('completed'),
                'TASK_TITLE': task.get('title'),
            })
    csvfile.close()
    print("File {}.csv created successfully".format(user_id))
