#!/usr/bin/env python
"""
Determine the number or shortest paths between two points.

The area of the two points is determined by the user inputting a number of rows and a number of columns.
The starting position is in the in the top left corner and the end point is in the bottom right.
The program will calculate how many unique paths there are they take the least number of steps to
reach the end point.  Each step must be either to the right or down.  For example:

A 3 x 4 area would be (S = start, F = finish):
 _ _ _ _
|S| | | |
| | | | |
| | | |F|

Utilizes a "top down" solution to solve the subproblem first.
"""

from Helpers.helper_functions import show_new_example, repeat_example

___author___ = "Neil Doherty"

def validate_integer(user_input):
    try:
        converted_int = int(user_input)
        if converted_int <= 0:
            print("Input must be greater than 0.\n")
            return False, -1
        return True, converted_int
    except ValueError as error:
        print("Invalid input.  Please input an integer greater than 0.")
        return False, -1

def get_user_input():
    is_valid_input = False
    while not is_valid_input:
        row_input = input("Enter the number of rows in the play area: \n")

        valid_rows, num_rows = validate_integer(row_input)
        if not valid_rows:
            continue

        column_input = input("Enter the number of columns in the play area: \n")
        valid_columns, num_columns = validate_integer(column_input)
        if not valid_columns:
            continue

        return num_rows, num_columns

# Since the first move on the path will always be either 1 row down or 1 column right,
# the formula for determining the number of shortest paths will be recursively adding
# the full number of columns + (rows - 1) + the full number of rows + (columns - 1)
def get_num_shortest_paths(rows, cols, memo_rows={}, memo_cols={}):
    # Base case to return when rows or cols = 1
    if rows == 1 or cols == 1:
        return 1

    # Correct but inefficient solution:
    # return get_num_shortest_paths(rows - 1, cols) + get_num_shortest_paths(rows, cols - 1)

    # Optimized solution using memoization
    if not rows in memo_rows:
        memo_rows[rows] = get_num_shortest_paths(rows - 1, cols)

    if not cols in memo_cols:
        memo_cols[cols] = get_num_shortest_paths(rows, cols - 1)

    return memo_rows[rows] + memo_cols[cols]


def start_shortest_paths():
    finished = False
    while not finished:
        print("This function calculates the quantity of shortest possible paths between two points.\n"
              "The area is determined by your input for the number of rows and columns for the\n"
              "rectangle. The starting point is always in the top left corner and the end is the \n"
              "bottom right corner.  The steps taken on the path are always either down or right.\n")

        rows, columns = get_user_input()
        print("Using the %i rows and %i columns the shortest path will take %i steps."
              % (rows, columns, ((rows - 1) + (columns - 1))))
        num_of_paths = get_num_shortest_paths(rows, columns)
        print("The number of paths that take the least number of steps is %i" % num_of_paths)
        repeat = repeat_example()

        if repeat:
            continue
        else:
            return show_new_example()