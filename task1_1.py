#!/usr/bin/env python3

"""script accepts the file name and puts its extension to output.
If there is no extension - an exception should be raised."""


import os
import sys


def get_input_file():
    """Function gets input_file."""
    input_file = ""
    while input_file == "":
        input_file = input("Enter the file name\n")
    return input_file


def get_file_extension(input_file):
    """Function gets File Extension."""
    try:
        basename, extension = os.path.splitext(input_file)
        if not extension:
            raise ValueError("File has no extension.")
        print("The extension of the file is " + extension)

    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    get_file_extension(get_input_file())
