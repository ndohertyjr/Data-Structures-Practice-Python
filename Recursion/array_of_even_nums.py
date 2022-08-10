#!/usr/bin/env python
"""
Example of recursively creating an array of even nums from an existing array.

Utilizes a "top down" solution to solve the subproblem.
"""

from Helpers.helper_functions import show_new_example, repeat_example

___author___ = "Neil Doherty"


# Validate that input is an int
def validate_input(input):
    is_negative = False

    if not input:
        return False, 0

    if input[0] == '-':
        is_negative = True
        input = input[1:len(input)]

    try:
        valid_int = int(input)
        print(type(valid_int))
        if is_negative:
            valid_int = valid_int * -1
        return True, valid_int
    except ValueError as error:
        print("Error during validation. Error: %s" % error)
        return False, 0


# Creates original array to be used when converting to an all even number array
def build_original_array(original_array):
    is_complete = False

    while not is_complete:
        user_input = input(
            "Enter any integer from -2147483648 through 2147483647. "
            "Type \"/run\" to execute the function. ") \
            .strip().lower()

        if user_input == "/run":
            return original_array

        # Validate that input is an valid int
        is_valid, num = validate_input(user_input)

        if is_valid:
            original_array.append(num)
        else:
            print("User input was not valid.  Try again.\n")



# Using original array, build new array with only even numbers
def build_even_array(original_array, even_num_array):
    # Determine if current value is even and add to the new array
    if original_array[0] % 2 == 0:
        even_num_array.append(original_array[0])

    # base case to return when there is only one item in the array
    if len(original_array) == 1:
        return even_num_array
    else:
        build_even_array(original_array[1:len(original_array)], even_num_array)



def start_array_of_even_nums():
    print("This example will build a new array of only the even numbers in an existing array.")
    print("Begin by entering digits to build the existing array.")
    original_array = []
    even_num_array = []
    build_original_array(original_array)
    build_even_array(original_array, even_num_array)
    print(original_array)
    print(even_num_array)

    repeat = repeat_example()

    if repeat:
        start_array_of_even_nums()
    else:
        return show_new_example()
