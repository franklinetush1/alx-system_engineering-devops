#!/usr/bin/python3
"""Returns to-do list information"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    idval = int(sys.argv[1])
    user = requests.get(url + 'users/{}'.format(idval)).json()
    task_list = requests.get(url + 'todos').json()
    totaltask = 0
    completed = []
    for i in range(len(task_list)):
        if task_list[i].get('userId') == idval:
            totaltask += 1
            if task_list[i].get('completed') is True:
                completed.append(task_list[i].get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completed), totaltask))
    [print("\t {}".format(task)) for task in completed]
