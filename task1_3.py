#!/usr/bin/env python3

#Script reads the access log from a file. 
#The name of the file is provided as an argument. 
#An output of the script provides the total number of different User Agents 
#and then provides statistics with the number of requests from each of them.


import sys
import re

dir_log = {}
count_log = 0

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
                name = re.search(r'"(Mozilla.+)"$', line).group(1)
                if name not in dir_log:
                    dir_log[name] = 0
                    count_log += 1
                dir_log[name] += 1
    print(f"The total number of different User Agents: {count_log}")
    for x in dir_log:
        print (x,':', dir_log[x])

