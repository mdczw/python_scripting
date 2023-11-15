#!/usr/bin/env python3

"""Script removes duplicates from the list and create a tuple.
Finds the minimum and maximum number."""

import sys


def minimum_value (number_list):
    """function finds the minimum value"""
    min_number = number_list[0]

    for number in number_list:
        if number < min_number:
            min_number = number
    return min_number


def maximum_value(number_list):
    """function finds the maximum value"""
    max_number = number_list[0]

    for number in number_list:
        if number > max_number:
            max_number = number
    return max_number


def get_list_of_numbers_from_input():
    """function gets the list from the user"""
    user_input = ""
    while user_input == "":
        user_input = input("Enter a list of numbers separated by commas:\n")

    try:
        number_list = [int(num.strip()) for num in user_input.split(",")]

    except ValueError as err:
        print(f"Error {err}")
        print("Example list of numbers: -1, 1, -6, -6, 25, 100, 3, 6, 3, 5, 6, 1")
        sys.exit(1)
    else:
        return number_list


def tuple_without_duplicates(number_list):
    """function creates a tuple without duplicates"""
    return tuple(set(number_list))


if __name__ == "__main__":

    original_list = get_list_of_numbers_from_input()
    tuple_numbers = tuple_without_duplicates(original_list)

    print(f"Original list: {str(original_list)}")
    print(f"Tuple without duplicates: {str(tuple_numbers)}")
    print(f"The maximum number is {str(maximum_value(tuple_numbers))}")
    print(f"The minimum number is {str(minimum_value(tuple_numbers))}")
