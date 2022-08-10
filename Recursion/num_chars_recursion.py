#!/usr/bin/env python
"""
Example of recursively calculating the numbers of characters in an array of strings.

Utilizes a "top down" solution to solve the subproblem first.
"""

from Helpers.helper_functions import show_new_example

___author___ = "Neil Doherty"

# Accept user input.  Potentially add better menu return
def input_strings(array):
    current_string = input("Enter a string that is at least 1 character and less than 20 characters: ")

    if len(current_string) < 1:
        print("String must contain at least one character")
    elif len(current_string) >= 20:
        print("String must be less than 20 characters")
    else:
        array.append(current_string)

    add_more_strings = input("Enter any key to add more strings or type \"/run\" to execute the function.")

    if add_more_strings == "/run":
        return array
    else:
        input_strings(array)


def calculate_chars_in_array(array, index = 0):
    # base case to return length of final array value
    if len(array) == 1:
        return len(array[0])

    # return current string length + every other string in the array
    return len(array[0]) + calculate_chars_in_array(array[1:len(array)])



def repeat_example():
    repeat = input("Would you like to try a new array? (Y/N): ").upper().strip()

    if repeat == "Y":
        start_num_chars_recursion()
    elif repeat == "N":
        return
    else:
        print("Invalid selection. Try again.")
        repeat_example()


def start_num_chars_recursion():
    print("Begin by entering strings to use in the array.  When finished, enter \"/run\" to being the function.")

    array = []
    input_strings(array)
    num_of_chars = calculate_chars_in_array(array)

    print("\nYour array is:")
    print(array)
    print("\nThe number of characters in the array is:\n%s\n" % num_of_chars)

    repeat_example()

    return show_new_example()