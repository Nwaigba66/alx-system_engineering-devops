#!/usr/bin/python3
"""
This script fetches response from an API and exports data in CSV format
"""
import csv
import requests
import sys


def export_todos_to_csv(employee_id):
    """
    Returns info about an employee's TODO list progress
    """
    id_endpoint = "https://jsonplaceholder.typicode.com/users/" + employee_id
    todos_endpoint = id_endpoint + "/todos"
    try:
        response = requests.get(id_endpoint)
        user_data = response.json()
        username = user_data.get('username')
        response = requests.get(todos_endpoint)
        todos = response.json()

        # Create a CSV file
        csv_filename = employee_id + ".csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            for todo in todos:
                task_completed_status = str(todo.get('completed'))
                task_title = todo.get('title')
                csv_file.write('"{}","{}","{}","{}"\n'.format(
                    user_data.get("id"),
                    username,
                    task_completed_status,
                    task_title))
    except Exception:
        print("Something went wrong.")


if __name__ == "__main__":
    # check if input is an integer
    employee_id = sys.argv[1]
    export_todos_to_csv(employee_id)
