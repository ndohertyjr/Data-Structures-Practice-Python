#!/usr/bin/env python
"""
Example of recursively calculating triangular numbers.
Accepts user input for an index (N) and identifies the correct value based on the input
using the formula: value = N + valueof(N-1)

Utilizes a "top down" solution to solve the subproblem first.
"""

from Helpers.helper_functions import show_new_example, repeat_example

___author___ = "Neil Doherty"


def get_user_input():
    is_valid_input = False
    while not is_valid_input:
        user_input = input("Enter an integer > 0 to calculate the value at that index and see the sequence.\n")
        try:
            index = int(user_input)
            if index < 0:
                print("Input must be greater than 0.")
                continue
            else:
                return index
        except ValueError as error:
            print("Error converting to integer. Only integers > 0 may be entered.")
            continue

def calculate_triangular_num(index):
    # Base case to return when index is 0
    if index == 0:
        return index

    return index + calculate_triangular_num(index - 1)


def start_triangular_nums():
    print("A triangular number sequence is where the next value in the sequence is\n"
          "determined by the current index and the value of the number in the prior index.\n")
    print("\nEnter an index and the program will print the triangular number\n"
          "value based on the index you entered.\n")
    index = get_user_input()

    print("The value at index %i is %i" % (index, calculate_triangular_num(index)))

    repeat = repeat_example()

    if repeat:
        start_triangular_nums()
    else:
        show_new_example()