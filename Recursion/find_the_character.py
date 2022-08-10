#!/usr/bin/env python
"""
Function that accepts a string containing an 'x' and returns the index of the first occurrence

Utilizes a "top down" solution to solve the subproblem first.
"""

from Helpers.helper_functions import show_new_example, repeat_example

___author___ = "Neil Doherty"


def get_user_char():
    is_valid = False
    while not is_valid:
        user_input = input("Enter a character to search for: ").strip().lower()

        if len(user_input) == 1:
            return user_input
        else:
            print("Invalid entry.  Only enter one character.")
            continue


def get_user_string():
    is_valid = False
    while not is_valid:
        user_input = input("Enter the string you would like to search: ").strip().lower()

        if not user_input:
            print("No string detected.  Please enter a valid string.")
            continue
        else:
            return user_input


def find_instance_of_char(user_char, user_string, index=0):
    # Base case to return at the end of the string
    if index == len(user_string) - 1:
        if user_char == user_string[index]:
            return index
        else:
            return -1

    if user_char == user_string[index]:
        return index
    else:
        return find_instance_of_char(user_char, user_string, index + 1)


def start_find_the_character():
    finished = False
    while not finished:
        print("Enter a character and a string and the program will return the index of\n"
              "the first instance of that character regardless of case.\n")

        char_input = get_user_char()
        string_input = get_user_string()

        index_of_char = find_instance_of_char(char_input, string_input)

        if index_of_char > 0:
            print("Character instance located at index %i" % index_of_char)
        else:
            print("No instance of \"%s\" located in the string \"%s\"." % (char_input, string_input))

        repeat = repeat_example()

        if repeat:
            continue
        else:
            return show_new_example()
