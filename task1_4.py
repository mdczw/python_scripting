#!/usr/bin/env python3

"""Given an input string, count occurrences of all characters within a string"""

def get_string_from_input():
    """Function gets string from input"""
    string = ""

    while string == "":
        string = input("Give me a string and I'll count occurrences of all characters\n")
    return string

def character_counter(string):
    """Function counts occurrences of all characters within a string"""
    counter={}

    for character in string:
        if character.lower() in counter:
            counter[character.lower()] += 1
        else:
            counter[character.lower()] = 1
    return counter


if __name__ == "__main__":

    print(str(character_counter(get_string_from_input())))
