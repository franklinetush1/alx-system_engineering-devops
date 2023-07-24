#!/usr/bin/python3
import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = int(sys.argv[1])
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    task_list = requests.get(url + 'todos').json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in task_list:
            if task['userId'] == user_id:
                completed_status = "True" if task['completed'] else "False"
                writer.writerow([user_id, user['name'], completed_status, 
                                task['title']])
