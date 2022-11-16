#!/usr/bin/python3

"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    # get employee response
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()

    # get total number of tasks
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    # get number completed tasks
    completed = [todo.get("title") for todo in todos if todo.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
