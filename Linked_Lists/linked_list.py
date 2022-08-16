#!/usr/bin/env python
"""
Example of creating a linked list and common functions within the class

For sake of the example, all classes will be in this file though this is generally
not the best practice.
"""

from Helpers.helper_functions import show_new_example, repeat_example
import random

__author__ = "Neil Doherty"

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:

    def __init__(self, node=None):
        self.head = node

    def num_items_in_list(self):
        current_node = self.head
        num_items = 0
        while current_node is not None:
            num_items += 1
            current_node = current_node.next_node

        return num_items

    def add_node_to_end(self, node_data):
        new_node = Node(node_data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next_node is not None:
            current_node = current_node.next_node

        current_node.next_node = new_node

    # Insertion anywhere in between the beginning and end of list
    def add_node_at_index(self, node_data, add_index):
        new_node = Node(node_data)
        current_node = self.head
        current_index = 0
        while current_node.next_node is not None:
            if add_index == 0:
                new_node.next_node = self.head
                self.head = new_node
                return
            if current_index == add_index - 1:
                temp_next_node = current_node.next_node
                current_node.next_node = new_node
                current_node.next_node.next_node = temp_next_node
                return
            elif current_index == add_index:
                temp_next_node = current_node
                current_node = new_node
                current_node.next_node = temp_next_node

            current_node = current_node.next_node

            current_index += 1

        # Index not found within the length of the list
        print("Index selected is greater than number of items in the list.\n"
              "Please use the Add Node To End Of List command.")

    # Find an item by the index in the list
    def get_item_at_index(self, index_input):
        current_node = self.head
        current_index = 0
        while current_node is not None:
            # Prints and returns when index is found
            if current_index == index_input:
                self.print_node(current_node)
                return current_node
            else:
                current_index += 1
                current_node = current_node.next_node

        # Prints if index is not found
        print("Index not located within the list.  Please confirm your index is in range.")

    # Get the last item in the list assuming the number of items in list was not known
    def get_last_item(self):
        current_node = self.head

        while current_node.next_node is not None:
            current_node = current_node.next_node

        self.print_node(current_node)

    def reverse_list(self):
        dict_of_nodes = {}
        index = 0
        current_node = self.head

        # Store all nodes in a dictionary for quick lookup
        while current_node is not None:
            dict_of_nodes[index] = current_node
            current_node = current_node.next_node
            index += 1

        # Create new linked list using dictionary
        reversed_list = LinkedList()
        for num in range(index - 1, -1, -1):
            reversed_list.add_node_to_end(dict_of_nodes[num].data)

        reversed_list.print_list()

    def print_list(self):
        current_node = self.head

        while current_node is not None:
            self.print_node(current_node)
            current_node = current_node.next_node

    @staticmethod
    def print_node(node):
        print("-----------------------------------------------")
        print("Current Node data: %s" % node.data)
        print("Current Node memory address is: %s" % id(node))
        print("Next Node's memory address is %s\n" % id(node.next_node))
        print("-----------------------------------------------")


def get_user_input(linked_list):

    list_build_selection_done = False
    items_for_prebuilt_list = ["This", "is", "a", "linked", "list"]
    while not list_build_selection_done:
        user_choice = input("Enter 1 to create your own linked list or 2 for a generated one:\n")
        if user_choice == "1":
            print("To create your own list, please enter any string.  Type \"/done\" when finished.")
            finished_adding = False
            while not finished_adding:
                string_input = input("Enter a string to be added to the list or enter \"/done\" to finish:\n").strip()

                if string_input == "/done":
                    return

                linked_list.add_node_to_end(string_input)
        elif user_choice == "2":
            print("Generating linked list...")
            for item in items_for_prebuilt_list:
                linked_list.add_node_to_end(item)
            print("Complete!")
            return
        else:
            print("Invalid selection.")

# Still under progress

def puzzle_problem(linked_list):
    print("The function that will run when you press enter is to solve the below problem:\n\n")
    print("\"You have access to a node in the middle of a linked list, but not the linked list itself.\n"
          "That is you have a variable that points to an instance of Node, but you don't have access to\n"
          "the LinkedList instance.  If you follow the nodes link, you can find all the items from\n"
          "this middle node until the end, but you have no way to find the nodes that precede this node\n"
          "in the list.  Write a function that will effectively delete this node from the list while\n"
          "keeping the remaining nodes in the list complete.\"\n"
          "From pg 245 of A Common Sense Guide to Data Structures and Algorithms by Jay Wengrow\n")

    print("This will use the current list you have established to simulate the problem.  The node you have\n"
          "access to is:")

    # Using list instance to get a random starting point.  Instance not used again to remove the node.
    random_index = random.randint(0, linked_list.num_items_in_list() - 1)
    node = linked_list.get_item_at_index(random_index)
    print(linked_list.print_node(node))

    input("Press enter to remove the node from the list...")

    while node is not None:
        if node.next_node is None:
            node = None
            break
        else:
            print("%s is becoming %s" % (node.data, node.next_node.data))
            node.data = node.next_node.data
            node = node.next_node



    print("Deleted!")
    linked_list.print_list()

def get_index_selection(instructions):
    is_complete = False
    while not is_complete:
        try:
            user_input = input(instructions)
            converted_input = int(user_input)
            return converted_input
        except ValueError as error:
            print("Input error.  Selection must be an int.  Try again.")

def start_linked_list():
    finished = False
    while not finished:
        linked_list = LinkedList()
        print("This example will demonstrate a variety of functions when using the Linked List\n"
              "data structure.  For reference, the Linked List's time complexity during different\n"
              "tasks is:\n"
              "Reading: O(N)\n"
              "Search: O(N)\n"
              "Insertion: O(1) at beginning, O(N) elsewhere\n"
              "Deletion: O(1) at beginning, O(N) elsewhere\n")

        get_user_input(linked_list)
        is_using_current_list = False
        while not is_using_current_list:
            print("Choose a function to perform on the current linked list:\n"
                  "1. Add item to the end of the list\n"
                  "2. Add item at an index within the list\n"
                  "3. Read item at a specific index\n"
                  "4. Print all items in the list\n"
                  "5. Print the last item in the list\n"
                  "6. Reverse the list order\n"
                  "7. Puzzle Problem")
            user_choice = input("Selection: ")

            if user_choice == "1":
                string_input = input("Enter a string to be added to the list:\n").strip()
                linked_list.add_node_to_end(string_input)
            elif user_choice == "2":
                string_input = input("Enter a string to be added to the list:\n").strip()
                index_input = get_index_selection("Enter the index within the current list where the string will be inserted:\n")
                linked_list.add_node_at_index(string_input, index_input)
            elif user_choice == "3":
                index_input = get_index_selection("Enter the index of the item you would like to find:\n")
                linked_list.get_item_at_index(index_input)
            elif user_choice == "4":
                linked_list.print_list()
            elif user_choice == "5":
                linked_list.get_last_item()
            elif user_choice == "6":
                linked_list.reverse_list()
            elif user_choice == "7":
                puzzle_problem(linked_list)
            else:
                print("Invalid selection.")

        repeat = repeat_example()

        if repeat:
            continue
        else:
            return show_new_example()
