#!/usr/bin/python3

"""Exports to-do list information for a given employee ID to JSON format."""
from sys import argv
from requests import get
import json


if __name__ == "__main__":
    usr_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    usr = get(url + "users/{}".format(usr_id)).json()
    username = usr.get("username")
    todos = get(url + "todos", params={"userId": usr_id}).json()

    with open("{}.json".format(usr_id), "w") as file:
        json.dump({usr_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, file)
