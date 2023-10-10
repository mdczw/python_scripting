#!/usr/bin/env python3

"""Given an input string, count occurrences of all characters within a string"""

string = ""

while string == "":
    string = input("Give me a string and I count occurrences of all characters\n")

counter={}

for character in string:
    if character.lower() in counter:
        counter[character.lower()] += 1
    else:
        counter[character.lower()] = 1
print(str(counter))
