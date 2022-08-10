#!/usr/bin/env python
"""
Example of recursively calling a function to traverse an array
"""

from Helpers.helper_functions import show_new_example, repeat_example

___author___ = "Neil Doherty"


array = [
    1,
    2,
    3,
    [4, 5, 6],
    7,
    [8,
        [9, 10, 11,
            [12, 13, 14]
        ]
    ],
    [15, 16, 17, 18, 19,
        [20, 21, 22,
            [23, 24, 25,
                [26, 27, 28]
            ], 29, 30
        ], 31
    ]
]

def array_recursion(current_array):
    for item in current_array:
        # Function checks if item is a list, if so calls function recursively
        if type(item) == list:
            print("Array detected, traversing array of size %s" % (len(item)))
            array_recursion(item)
        else:
            print(item)

def start_array_recursion():
    print("ARRAY RECURSION EXAMPLE:")
    print("This example will show how the program can use recursion to traverse an array.\n")
    array_recursion(array)
    repeat = repeat_example()

    if repeat:
        start_array_recursion()
    else:
        return show_new_example()