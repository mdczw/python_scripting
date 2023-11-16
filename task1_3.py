#!/usr/bin/env python3

"""Script reads the access log from a file.
The name of the file is provided as an argument.
An output of the script provides the total number of different User Agents
and then provides statistics with the number of requests from each of them."""


import sys
import re


def get_file():
    """Gets a file if it exists"""
    try:
        file = sys.argv[1]
        return file

    except IndexError as err:
        print(f"Error: {err}")
        print(f"Usage: {sys.argv[0]} [log_file]")
        sys.exit(1)


def get_request_statistics(file):
    """Returns a dictionary with the number of requests from each of the user agents"""
    statistics = {}
    try:
        with open(file, encoding="utf-8") as f:
            for line in f.readlines():
                if "Mozilla" in line:
                    user_agent = re.search(r'"(Mozilla.+)"$', line).group(1)
                    if user_agent not in statistics:
                        statistics[user_agent] = 0
                    statistics[user_agent] += 1
        return statistics

    except FileNotFoundError as err:
        print(f"Error: {err}")
        sys.exit(1)


if __name__ == "__main__":

    log_file = get_file()
    request_statistics = get_request_statistics(log_file)

    print(f"Total number of different User Agents: {len(request_statistics)}")

    print("Number of requests from each of the User Agent:")
    for agent, counter in request_statistics.items():
        print(f"{agent}: {counter}")
