#!/usr/bin/env python
"""
Example of recursively calculating the numbers of characters in an array of strings.

Utilizes a "top down" solution to solve the subproblem first.
"""

from Helpers.helper_functions import show_new_example, repeat_example

___author___ = "Neil Doherty"

# Accept user input.  Potentially add better menu return
def input_strings(array):
    is_complete = False

    while not is_complete:
        current_string = input("Enter a string that is at least 1 character and less than 20 characters: \n")

        if len(current_string) < 1:
            print("String must contain at least one character")
            continue
        elif len(current_string) >= 20:
            print("String must be less than 20 characters")
            continue
        elif not current_string:
            print("String cannot be empty")
            continue
        else:
            array.append(current_string)
            add_more_strings = input("Enter any key to add more strings or type \"/run\" to execute the function.\n")

            if add_more_strings == "/run":
                is_complete = True
                return array


def calculate_chars_in_array(array):
    # base case to return length of final array value
    if len(array) == 1:
        return len(array[0])

    # return current string length + every other string in the array
    return len(array[0]) + calculate_chars_in_array(array[1:len(array)])


def start_num_chars_recursion():
    finished = False
    while not finished:
        print("Begin by entering strings to use in the array.  When finished, enter \"/run\" to being the function.")

        array = []
        input_strings(array)
        num_of_chars = calculate_chars_in_array(array)

        print("\nYour array is:")
        print(array)
        print("\nThe number of characters in the array is:\n%s\n" % num_of_chars)

        repeat = repeat_example()

        if repeat:
            continue
        else:
            return show_new_example()
