#!/usr/bin/env python
"""
Program shows different iterations of O(N) when searching for the greatest value in an array.

For example sake, all classes will be kept in this file.  This is bad system design, don't do this in real life.
"""

from Helpers.helper_functions import show_new_example, repeat_example
import time

__author__ = "Neil Doherty"


# Uses two for-loops to iterate over every value in the array and compare
# them together.  Very inefficient.


class ONSquared:

    array = []
    start_time = time.perf_counter()

    def __init__(self, array):
        self.array = array

    def find_greatest_value(self):
        highest_value = self.array[0]
        start_time = time.perf_counter()
        for first_int in range(0, len(self.array) - 1):
            if self.array[first_int] > highest_value:
                highest_value = self.array[first_int]
            for secondInt in range(first_int + 1, len(self.array)):
                if self.array[secondInt] > highest_value:
                    highest_value = self.array[secondInt]
        end_time = time.perf_counter()
        return highest_value, (end_time - start_time)


# Stores the highest number as every value in the array is iterated over once.  Returns the
# highest value found.  Reliable time as it is based on the number of items in the array
class ON:

    array = []

    def __init__(self, array):
        self.array = array

    def find_greatest_value(self):
        highest_value = self.array[0]
        start_time = time.perf_counter()
        for number in self.array:
            if number > highest_value:
                highest_value = number

        end_time = time.perf_counter()

        return highest_value, (end_time - start_time)


# Sorts the array using quick sort algorithm and then locates the final element.
class ONlogN:

    array = []

    def __init__(self, array):
        self.array = array

    def find_greatest_value(self):
        start_time = time.perf_counter()
        self.quicksort()
        highest_value = self.array[len(self.array) - 1]
        end_time = time.perf_counter()

        return highest_value, (end_time - start_time)

    def quicksort(self, left_index, right_index):
        if right_index - left_index <= 0:
            return

        pivot_point = self.partition_array(left_index, right_index)
        self.quicksort(left_index, pivot_point - 1)
        self.quicksort(pivot_point + 1, right_index)

    def partition_array(self, left_index, right_index):
        pivot_index = right_index
        pivot_value = self.array[pivot_index]
        right_index = right_index - 1

        while True:
            while self.array[left_index] < pivot_value:
                left_index += 1

            while self.array[right_index] > pivot_value:
                right_index -= 1

            if left_index >= right_index:
                break

            # Swap values that are on the wrong side of the pivot value
            temp_left = self.array[left_index]
            self.array[left_index] = self.array[right_index]
            self.array[right_index] = temp_left
            left_index += 1

        self.array[pivot_index] = self.array[left_index]
        self.array[left_index] = pivot_value

        return left_index


def get_array_input(array):
    is_complete = False
    while not is_complete:
        user_input = input("Enter any integer or \"/done\" to execute the program:\n")

        if user_input == "/done":
            if len(array) < 1:
                print("Array requires at least one integer.")
                continue

            break

        try:
            num = int(user_input)
            array.append(num)
        except ValueError as error:
            print("Input should be an integer.")


def start_different_interations_of_O():
    finished = False
    while not finished:
        # Code for the example here
        print("This program will find the greatest value within an array using different O(N) speeds.\n"
              "Begin by creating the array of integers.")
        num_array = []
        # get_array_input(num_array)
        for i in range(0, 10000):
            num_array.append(i)
        print("Your array is:")
        print(num_array)

        is_done_testing = False
        while not is_done_testing:
            print("Enter number of the time complexity you would like to use to determine the greatest value:")
            user_choice = input("1: O(N^2), 2: O(N), 3: O(NlogN) or \"/done\" to exit.\n").strip()
            if user_choice == "1":
                value_finder = ONSquared(num_array)
                highest_value, run_time = value_finder.find_greatest_value()
                print("The highest value in the array is:")
                print(highest_value)
                print(f"It took {run_time:0.6f} seconds to search for the value.")

            elif user_choice == "2":
                value_finder = ON(num_array)
                highest_value, run_time = value_finder.find_greatest_value()
                print("The highest value in the array is:")
                print(highest_value)
                print(f"It took {run_time:0.6f} seconds to search for the value.")

            elif user_choice == "3":
                value_finder = ON(num_array)
                highest_value, run_time = value_finder.find_greatest_value()
                print("The highest value in the array is:")
                print(highest_value)
                print(f"It took {run_time:0.6f} seconds to search for the value.")

            elif user_choice == "/done":
                break

            else:
                print("Invalid selection.  Please choose 1, 2, or 3.")

            retry = input("Try other time complexities on the same array? (Y/N)\n").upper().strip()
            if retry == "Y":
                continue
            elif retry == "N":
                is_done_testing = True
            else:
                print("Invalid selection, showing time complexity options again.")

        repeat = repeat_example()

        if repeat:
            continue
        else:
            return show_new_example()
