#!/usr/bin/env python3

#script accepts the file name and puts its extension to output. 
#If there is no extension - an exception should be raised.


import os
import sys

input_file=''
while input_file =='':
    input_file = input("Enter the file name\n")

try:
    basename, extension = os.path.splitext(input_file)
    if not extension:
        raise ValueError("File has no extension.")
    print("The extension of the file is " + extension)

except ValueError as e:
    print(f"Error: {e}")
    sys.exit(1)
