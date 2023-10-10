#!/usr/bin/env python3

import os
import sys

try:
    input_file = input("Enter the file name\n")
    basename, extension = os.path.splitext(input_file)
    if not extension:
        raise ValueError("File has no extension.")
    print("The extension of the file is " + extension)

except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)
