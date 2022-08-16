#!/usr/bin/env python
"""
Data Structures and Algorithms Examples

Contains a variety of different DS&A examples and explanation comments to better
understand what is happening in the code and why.
"""

from Recursion.array_recursion import start_array_recursion
from Recursion.num_chars_recursion import start_num_chars_recursion
from Recursion.array_of_even_nums import start_array_of_even_nums
from Recursion.triangular_nums import start_triangular_nums
from Recursion.find_the_character import start_find_the_character
from Recursion.shortest_paths import start_shortest_paths
from Recursion.dont_exceed_100 import start_dont_exceed_100
from Recursion.golomb_sequence import start_golomb_sequence
from Sorting.product_of_three_nums import start_product_of_three_nums
from Sorting.find_missing_number import start_find_missing_num
from Sorting.different_iterations_of_O import start_different_interations_of_O
from Linked_Lists.linked_list import start_linked_list

___author___ = "Neil Doherty"

# Menu Selection options
menu_options = {
    "recursion": {
        "1": ["Traverse and array with recursion", start_array_recursion],
        "2": ["Number of characters in array of strings", start_num_chars_recursion],
        "3": ["Build an array of even numbers", start_array_of_even_nums],
        "4": ["Calculate triangular number based on index", start_triangular_nums],
        "5": ["Find the character in the string", start_find_the_character],
        "6": ["Find number of shortest paths", start_shortest_paths],
        "7": ["Add an array of numbers until it reaches 100", start_dont_exceed_100],
        "8": ["Golomb sequence", start_golomb_sequence]
    },
    "sorting": {
        "1": ["Find the greatest product of three numbers from an array", start_product_of_three_nums],
        "2": ["Find the missing number in an array", start_find_missing_num],
        "3": ["Different O(N) iterations of sorting", start_different_interations_of_O]
    },
    "linked lists": {
        "1": ["Linked List example functions", start_linked_list]
    }
}


def welcome_menu():
    print("Welcome to the DS&A Example tool.\n")
    print("Choose from the following example programs:")
    message_selection()
    print("Thanks for coming. Have a good day!")



def message_selection():
    category_selection = "0"
    example_selection = "0"
    valid_category = False
    valid_example = False

    choose_new_example = True
    while choose_new_example == True:
        print("Select a category from the list below:")
        for category in menu_options:
            print(" - " + category)


        while valid_category == False:
            print("Type the name of the category you would like to explore (ex. recursion).")
            category_selection = input("Selection: ").lower().strip()
            if category_selection in menu_options:
                valid_category = True
            else:
                print("Invalid selection. Try again.")

        while valid_example == False:
            print("\nEnter the number of the example you want to see.  Type \"00\" to return to category selection")
            for example in menu_options[category_selection]:
                print(example + ". " + menu_options[category_selection][example][0])

            print("00. Return to category selection\n")
            example_selection = input("Example selection: ").strip()

            if str(example_selection) == "00":
                message_selection()

            if example_selection in menu_options[category_selection]:
                valid_example = True
            else:
                print("Invalid selection. Try again.")

        print("You chose the example of %s from the category %s" %
              (menu_options[category_selection][example_selection][0], category))
        print("\n***************************************************")
        print("***************************************************\n")

        choose_new_example = menu_options[category_selection][example_selection][1]()

        # Reset loop
        if choose_new_example == True:
            category_selection = ""
            example_selection = ""
            valid_category = False
            valid_example = False





if __name__ == '__main__':
    welcome_menu()


