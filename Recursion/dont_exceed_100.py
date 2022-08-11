#!/usr/bin/env python
"""
Calculates the sum of an array using only the integers that would not cause the sum to exceed 100
"""

from Helpers.helper_functions import show_new_example, repeat_example

___author___ = "Neil Doherty"


def get_array_nums(array):
    is_finished = False
    while not is_finished:
        user_input = input("Enter an integer for the array or enter \"/run\" to run the program.\n")

        if user_input == "/run":
            break
        try:
            user_int = int(user_input)
            array.append(user_int)
        except ValueError as error:
            print("Value must be an int.  Try again.")

def add_until_100(array):
    if len(array) == 0:
        return 0

    remaining_values = add_until_100(array[1:len(array)])

    if array[0] + remaining_values > 100:
        return remaining_values
    else:
        return array[0] + remaining_values

def start_dont_exceed_100():
    finished = False

    while not finished:
        print("This example will accept an array of numbers and return the sum of the numbers.\n"
              "Any number that would cause the sum to be greater than 100 is ignored.\n")
        num_array = []
        get_array_nums(num_array)

        print("Your array is:")
        print(num_array)
        print("\nDetermining array index where value exceeds 100...")
        answer = add_until_100(num_array)
        print("Sum of numbers that would not exceed 100 is:\n")
        print(answer)

        repeat = repeat_example()

        if repeat:
            continue
        else:
            return show_new_example()