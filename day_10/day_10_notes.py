# ------------------------------------------------------------------------------------------------ #
#                                      Functions with Outputs                                      #
# ------------------------------------------------------------------------------------------------ #


### Functions with output
# -- Functions can return back an output to be used elsewhere in the code
# -- the return keyword creates an output
def my_function():  # defining a function
    result = 3 * 2
    return result  # return keyword is used to return an output


output = my_function()  # the result is returned and saved to the output variable


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide any inputs."  # an early return (executed if f_name or l_name are empty)
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name("MarLON", "NuNez")
print(formatted_string)


### Docstrings
# -- Docstrings are used to write documentation or multi-line comments
# -- To create a docstring, use two sets of triple quotes (""" """)


def format_name2(f_name, l_name):
    """Take a first name and last name and format it to return the title-case version of the name"""
    if f_name == "" or l_name == "":
        return "You did not provide any inputs."  # an early return (executed if f_name or l_name are empty)
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


### print() vs return
# --print() is used to print something to the console
# --return is used to create an output that can be used later in the code (as an input to other functions)


### Recursion
# -- Recursion --> a function that has the ability to call itself
# -- MUST BE CAREFUL because recursive functions can lead to infinite loops (add a condition to exit or proceed)
