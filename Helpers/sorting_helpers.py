#!/usr/bin/env python
"""
Helper functions for sorting examples
"""

___author___ = "Neil Doherty"

# Partition for Quicksort/Quickselect/etc
# Partitions an array with all values smaller than the pivot to the left and all values
# greater than the pivot to the right.  Does not sort the partitions


class ArraySort:

    sorted_array = []

    def __init__(self, array):
        self.sorted_array = array

    def quicksort(self, left_index, right_index):
        if right_index - left_index <= 0:
            return

        pivot_point = self.get_partition(left_index, right_index)

        self.quicksort(left_index, pivot_point - 1)

        self.quicksort(pivot_point + 1, right_index)

    def get_partition(self, left_pointer, right_pointer):
        pivot_index = right_pointer
        pivot_val = self.sorted_array[pivot_index]
        right_pointer = pivot_index - 1


        while True:
            while self.sorted_array[left_pointer] < pivot_val:
                left_pointer += 1

            while self.sorted_array[right_pointer] > pivot_val:
                right_pointer -= 1

            if left_pointer >= right_pointer:
                break
            else:
                temp_value = self.sorted_array[left_pointer]
                self.sorted_array[left_pointer] = self.sorted_array[right_pointer]
                self.sorted_array[right_pointer] = temp_value
                left_pointer += 1

        temp_pivot = self.sorted_array[pivot_index]
        self.sorted_array[pivot_index] = self.sorted_array[left_pointer]
        self.sorted_array[left_pointer] = temp_pivot

        return left_pointer
