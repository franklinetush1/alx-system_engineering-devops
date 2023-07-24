#!/usr/bin/python3
"""Exports to-do list all employees to JSON format."""
import json
import requests


def fetch_user_data(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    user_data = response.json()
    return user_data['username']


def export_tasks_to_json():
    base_url = "https://jsonplaceholder.typicode.com/"
    users_response = requests.get(base_url + "users")
    users = users_response.json()

    data = {}
    for user in users:
        user_id = user.get("id")
        username = fetch_user_data(user_id)

        tasks_response = requests.get(base_url + "todos",
                                      params={"userId": user_id})
        tasks = tasks_response.json()

        task_data = []
        for task in tasks:
            task_data.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        data[user_id] = task_data

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)


if __name__ == "__main__":
    export_tasks_to_json()
