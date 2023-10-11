#!/usr/bin/env python3

'''Script removes duplicates from the list and create a tuple.
Finds the minimum and maximum number.'''

import sys

#num_list = [-1, 1, -6, -6, 25, 100, 3, 6, 3, 5, 6, 1]

user_input = ''
while user_input == '':
    user_input = input("Enter a list of numbers separated by commas:\n")

try:
    num_list = [int(num.strip()) for num in user_input.split(',')]

except ValueError as err:
    print(f"Error {err}")
    print("Example list of numbers: -1, 1, -6, -6, 25, 100, 3, 6, 3, 5, 6, 1")
    sys.exit(1)

else:
    tuple_list = tuple(set(num_list))

    max_num = tuple_list[0]
    min_num = tuple_list[0]

    for number in tuple_list:
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number

    print (f"Original list: {str(num_list)}")
    print (f"Tuple without duplicates: {str(tuple_list)}")
    print (f"The maximum number is {str(max_num)}")
    print (f"The minimum number is {str(min_num)}")
