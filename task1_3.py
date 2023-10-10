#!/usr/bin/env python3

import sys
import re

dir_log = {}

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
                dir_log[name] += 1

    for x in dir_log:
        print (x,':', dir_log[x])

