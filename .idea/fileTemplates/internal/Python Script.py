#!/usr/bin/env python
"""
Description of the exampled
"""

from Helpers.helper_functions import show_new_example, repeat_example

__author__ = "Neil Doherty"

def start_example_name_here():
    finished = False
    while not finished:
        # Code for the example here
        
        repeat = repeat_example()
        
        if repeat:
            continue
        else:
            return show_new_example()
            