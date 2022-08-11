#!/usr/bin/env python
"""
A representation of the Golomb Sequence using memoization.
"""

from Helpers.helper_functions import show_new_example, repeat_example

___author___ = "Neil Doherty"


def get_sequence_num():
    is_finished = False
    while not is_finished:
        user_input = input("Enter an integer >= 1 to run the program\n")

        try:
            user_int = int(user_input)
            if user_int < 1:
                print("Value must be >= 1.")
                continue
            return user_int
        except ValueError as error:
            print("Value must be an int.  Try again.")


def golomb(n, memo={}):
    if n == 1:
        return 1

    if not n in memo:
        memo[n] = golomb(n - golomb(golomb(n - 1, memo), memo), memo)

    return 1 + memo[n]


def start_golomb_sequence():
    finished = False

    while not finished:
        print("The Golomb Sequence is a monotonically increasing integer sequence where A_n is the number of\n"
              "time n occurs in the sequence starting with A_1 = 1.\n")

        user_input = get_sequence_num()
        print("The number of occurrences of %i in the sequence is:" % user_input)
        print(golomb(user_input))

        repeat = repeat_example()

        if repeat:
            continue
        else:
            return show_new_example()