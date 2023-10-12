#!/usr/bin/env python3

'''Script reads the access log from a file.
The name of the file is provided as an argument.
An output of the script provides the total number of different User Agents
and then provides statistics with the number of requests from each of them.'''


import sys
import re

request_statistics = {}
number_of_user_agents = 0

try:
    file = open(sys.argv[1])

except IndexError as err:
    print(f"Error: {err}")
    print(f"Usage: {sys.argv[0]} [log_file]")
    sys.exit(1)

except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)

else:
    with file:
        for line in file.readlines():
            if "Mozilla" in line:
                user_agent = re.search(r'"(Mozilla.+)"$', line).group(1)
                if user_agent not in request_statistics:
                    request_statistics[user_agent] = 0
                    number_of_user_agents += 1
                request_statistics[user_agent] += 1
    print(f"Total number of different User Agents: {number_of_user_agents}")
    print("Number of requests from each of the User Agent:")
    for x in request_statistics:
        print (f"{x}: {request_statistics[x]}")
