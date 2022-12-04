#!/usr/bin/python3

"""Exports to-do list information for a given employee ID to CSV format."""
from sys import argv
from requests import get
import csv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user = get(url + '/users/' + argv[1]).json()['username']
    todos = get(url + '/todos?userId=' + argv[1]).json()

    with open('{}.csv'.format(argv[1]), 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([argv[1], user, todo['completed'], todo['title']])
