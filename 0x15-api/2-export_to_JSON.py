import requests
import sys
import json


def export_tasks_to_json(tasks, user_id, username):
    data = {
        str(user_id): [
            {
                "task": task["title"],
                "completed": "True" if task["completed"] else "False",
                "username": username
            }
            for task in tasks
        ]
    }
    filename = f"{user_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    user_id = int(sys.argv[1])
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    task_list = requests.get(url + 'todos').json()

    user_tasks = [task for task in task_list if task.get('userId') == user_id]
    export_tasks_to_json(user_tasks, user_id, user['name'])