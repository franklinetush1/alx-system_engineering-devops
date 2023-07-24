#!/usr/bin/python3
"""Exports to-do list all employees to JSON format."""
import json
import requests


def export_tasks_to_json(url):
    def fetch_user_data(user_id):
        response = requests.get(url + f"users/{user_id}")
        return response.json()['name']

    response = requests.get(url + "todos")
    task_list = response.json()

    data = {}
    for task in task_list:
        user_id = task['userId']
        username = fetch_user_data(user_id)
        task_data = {
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
        }
        if user_id in data:
            data[user_id].append(task_data)
        else:
            data[user_id] = [task_data]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    export_tasks_to_json(url)
