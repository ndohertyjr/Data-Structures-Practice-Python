# Data-Structures-Practice-Python
Data Structures and Algorithms practice programs using Python

### How To Use
This is a command line program that will show working examples of different types of Data Structures and Algorithms.  Review the code to better understand the different examples.  To navigate the program simply follow the prompts and select the category and specific example you would like to see.


#### Menu Options
To add your own examples simple create the relevant .py file and add the start function to the options menu in main.py.  The helper functions in Helper.helper_functions.py can be added to your new .py file's starting function to handle repeating the same example or allowing the user return to the selection menu.

main.py
```
menu_options = {
    "recursion": {
        "1": ["Traverse and array with recursion", start_array_recursion],
        "2": ["Number of characters in array of strings", start_num_chars_recursion],
        "3": ["Build an array of even numbers", start_array_of_even_nums],
        "4": ["Calculate triangular number based on index", start_triangular_nums],
        "5": ["Find the character in the string", start_find_the_character],
        "6": ["Find number of shortest paths", start_shortest_paths]
    },
    "your_new_category": {
        "1": ["Example 1 text description", start_method_in_file]
        ...
    }
}
```
your_file.py helpers
```
def start_your_example():
    is_finished = False
    while not is_finished:
       
        # Orchestrate your example logic here
        
        # Helper functions:
        repeat = repeat_example()

        if repeat:
            continue
        else:
            return show_new_example()

```

##### Categories
The categories that contain examples currently are:

* Recursion

This is a work in progress and will continue to grow.

##### Examples for each category

* Recursion 
  * Traverse an array with recursion
  * Number of characters in an array of strings
  * Build an array of even numbers
  * Calculate triangular number based on index
  * Find the character in the string
  * Find number of shortest paths
