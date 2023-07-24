#!/usr/bin/python3
"""Exports to-do list information in CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    user_name = user.get("username")
    task_list = requests.get(url + 'todos').json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in task_list:
            if task['userId'] == int(user_id):
                completed_status = "True" if task['completed'] else "False"
                writer.writerow([user_id, user_name, completed_status,
                                task['title']])
