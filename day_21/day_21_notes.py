# ------------------------------------------------------------------------------------------------ #
#                                         Class Inheritance                                        #
# ------------------------------------------------------------------------------------------------ #

### Inheritance
# - Methods and Attributes can both be inherited


### Example - Class Inheritance
# Creating the parent class
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


# Creating a child class to inherit from parent
class Fish(Animal):  # Inheriting from Animal class
    def __init__(self):
        super().__init__()  # call super() on the init method

    def breathe(self):  # Taking the existing method from the parent class
        super().breathe()  # calling everything from parent's breathe() method
        print("doing this underwater")  # add more to breathe() method of child

    def swim(self):
        print("Moving in water")


# Creating an instance of Fish() class
nemo = Fish()
nemo.swim()

# Instance of Fish() has access to all properties and methods of parent class
nemo.breathe()
print(nemo.num_eyes)


### List & Tuple Slicing
# - Slicing allows you to grab a sub-section of a list or tuple
# -- Slicing includes the start, but excludes the stop

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[2:5])  # Slicing piano list from position 2-5
print(piano_keys[2:])  # Slicing piano list from position 2 to the end
print(piano_keys[2:5:2])  # Slicing piano list from position 2 to 5, skipping every 2
print(piano_keys[::2])  # Slicing paino list from begining to end, skipping every 2
print(
    piano_keys[::-1]
)  # Slicing piano list from the end to beginning (reverses the list)
