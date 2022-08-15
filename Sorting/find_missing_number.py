#!/usr/bin/env python
"""
Find the missing number in an array

The array should contain every number up to its length, except for one number.
Function will sort and search for the missing number to get a speed of O(N log N).

Program will generate the array and randomize the index of the ascending values.  Then it
will sort and determine which number is missing.
"""

from Helpers.helper_functions import show_new_example, repeat_example
from Helpers.sorting_helpers import ArraySort
import random

__author__ = "Neil Doherty"


def get_array_length_input():
    is_complete = False
    while not is_complete:
        length = input("Enter the length of the array to search: ")

        try:
            array_size = int(length)

            if array_size < 2:
                print("Array must have a length of 2 at least.")
            else:
                return array_size

        except ValueError as error:
            print("Input must be an integer >= 2.")


def get_missing_number(array_length):
    is_complete = False
    while not is_complete:
        num = input("Enter the number that should be missing or \"random\" for any number: ")

        if num == "random":
            missing_num = random.randrange(0, array_length)
            return missing_num
        else:
            try:
                missing_num = int(num)

                if missing_num < 0:
                    print("Value must be within the length of the array.")
                else:
                    return missing_num

            except ValueError as error:
                print("Input must be an integer > 0 and < array length.")


def build_array(array, length, missing_num_index):
    for i in range(length):
        if i == missing_num_index:
            continue
        else:
            array.append(i)

    random.shuffle(array)


def find_missing_num(array):
    # Partition array and continuing partitioning until sorted
    sorter = ArraySort(array)
    sorter.quicksort(0, len(array) - 1)

    for num in range(0, len(sorter.sorted_array) - 2):
        if sorter.sorted_array[num + 1] - sorter.sorted_array[num] == 1:
            continue
        else:
            return sorter.sorted_array[num] + 1


def start_find_missing_num():
    finished = False
    while not finished:
        # Code for the example here
        print("Program will determine the missing integer from an array given the length of the array\n"
              "and the index of the number that should be omitted.")
        num_array = []
        length = get_array_length_input()
        missing_number_index = get_missing_number(length)
        build_array(num_array, length, missing_number_index)
        print("Your array is: ")
        print(num_array)
        print("\nSorting and determining which number is missing...")
        missing_number = find_missing_num(num_array)
        print("The missing number is: ")
        print(missing_number)

        repeat = repeat_example()

        if repeat:
            continue
        else:
            return show_new_example()
