# ------------------------------------------
# 4. FUNCTIONS
# ------------------------------------------
# THEORY:
# What is a function and why do we use them?
# A function is a reusable block of code designed to perform a single, specific task. 
# We use functions to:
# 1. Keep our code organized and readable.
# 2. Avoid repetition (reusability) - define the code once, and call it many times.
# 3. Break down complex problems into smaller, manageable pieces that are easier to test.

# Example 1: Basic function with arguments and return value
# Functions are defined using the 'def' keyword. They package reusable code.
def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    area = length * width
    return area # Returns the calculated result back to the caller

print(f"Area of 5x4 rectangle: {calculate_area(5, 4)}")

# Example 2: Function with default parameter values
# If an argument is not provided when calling the function, it uses the default value.
def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_user("Alice")
greet_user("Bob", greeting="Hi")

# Example 3: Function with variable number of arguments (*args and **kwargs)
# *args allows passing a variable number of positional arguments (as a tuple)
# **kwargs allows passing a variable number of keyword arguments (as a dictionary)
def process_data(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

process_data(1, 2, 3, action="save", verbose=True)
