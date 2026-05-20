# ------------------------------------------
# 8. CLASSES AND OBJECTS (OOP)
# ------------------------------------------
# THEORY:
# What are classes and objects?
# Classes are blueprints for creating objects. They bundle data (attributes) and functions that
# operate on that data (methods) together. Objects are instances of a class.
# OOP helps us model real-world entities, manage complexity, and create reusable, modular code.

# Example 1: Defining a basic Class
# A class is a blueprint for creating objects (data structures that contain data and methods)
class Dog:
    # The __init__ method initializes the object's attributes when it's created
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    # Example 2: Adding a method to the class
    # Methods are functions that belong to the object
    def bark(self):
        print(f"{self.name} says Woof!")

# Example 3: Creating an Object (Instance) and using it
# Instantiating the class to create a specific object
my_dog = Dog("Buddy", "Golden Retriever")
print(f"My dog's name is {my_dog.name}.") # Accessing an attribute
my_dog.bark()                             # Calling a method
