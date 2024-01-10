# ------------------------------------------------------------------------------------------------ #
#                                        Function Parameters                                       #
# ------------------------------------------------------------------------------------------------ #

### Functions with inputs
#--Functions are helpful for performing repetitive actions
#--Parameters are variables used when defining the function
#--Arguments are the values of the data used when the function is called

# functions begin with the def keyword
def greet(name, birth_country, current_city): # parameters allow for the param to be passed into function for use
    print(f"My name is {name}.")
    print(f"I am from {birth_country}.")
    print(f"I live in {current_city}.")
    
greet("Marlon", "Costa Rica", "Boston") # calling the function with the arguments

