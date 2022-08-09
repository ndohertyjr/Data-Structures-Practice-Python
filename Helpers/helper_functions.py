#!/usr/bin/env python
"""
Helper functions to be used throughout the program
"""
___author___ = "Neil Doherty"


def show_new_example():
    user_choice = input("Would you like to see another example? (Y/N) ").upper().strip()

    if user_choice == "Y" or user_choice == "N":
        if user_choice == "Y":
            return True
        elif user_choice == "N":
            return False
    else:
        print("Invalid selection.  Please enter \"Y\" or \"N\"")
        show_new_example()
