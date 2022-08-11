#!/usr/bin/env python
"""
Helper functions to be used throughout the program
"""
___author___ = "Neil Doherty"


def show_new_example():
    is_finished = False
    while not is_finished:
        user_choice = input("Would you like to see another example? (Y/N) \n").upper().strip()

        if user_choice == "Y":
            return True
        elif user_choice == "N":
            return False
        else:
            print("Invalid selection.  Please enter \"Y\" or \"N\"")


def repeat_example():
    is_finished = False
    while not is_finished:
        repeat = input("Would you like to try this example again? (Y/N): \n").upper().strip()

        if repeat == "Y":
            return True
        elif repeat == "N":
            return False
        else:
            print("Invalid selection. Try again.")
