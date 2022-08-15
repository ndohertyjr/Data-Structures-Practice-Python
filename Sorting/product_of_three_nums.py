#!/usr/bin/env python
"""
Takes an array of positive nums and returns the greatest product of any three
"""



from Helpers.helper_functions import show_new_example, repeat_example
from Helpers.sorting_helpers import ArraySort

___author___ = "Neil Doherty"


def get_array_input(array):
    is_complete = False
    while not is_complete:
        user_input = input("Enter any positive integer or \"/run\" to execute the program:\n")

        if user_input == "/run":
            if len(array) < 4:
                print("Array requires at least 3 positive integers.")
                continue

            break

        try:
            num = int(user_input)
            if num <= 0:
                print("Enter a value greater than 0")
                continue
            array.append(num)
        except ValueError as error:
            print("Input should be an integer greater than 0.")


def get_greatest_product(array):
    # Using quicksort algorithm in Helpers.sorting_helpers.py, return sorted array
    array_helper= ArraySort(array)
    array_helper.quicksort(0, len(array) - 1)
    val1 = array_helper.sorted_array[len(array_helper.sorted_array) - 1]
    val2 = array_helper.sorted_array[len(array_helper.sorted_array) - 2]
    val3 = array_helper.sorted_array[len(array_helper.sorted_array) - 3]
    # Get highest values
    print("The three largest values are:\n")

    return val1 * val2 * val3


def start_product_of_three_nums():
    finished = False
    while not finished:
        print("Example will accept an array of at least 3 positive integers and returns the greatest product of any\n"
              "three numbers.\n")

        array_of_nums = []

        get_array_input(array_of_nums)
        print("You entered an array of:")
        print(array_of_nums)
        print("The greatest product of any three numbers is:")
        answer = get_greatest_product(array_of_nums)
        print(answer)

        repeat = repeat_example()

        if repeat:
            continue
        else:
            return show_new_example()