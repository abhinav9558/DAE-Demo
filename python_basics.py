# ==========================================
# PYTHON BASICS: EXAMPLES AND EXPLANATIONS
# ==========================================

# ------------------------------------------
# 1. VARIABLES AND DATA TYPES
# ------------------------------------------
# THEORY:
# Why do we have different variable types?
# In programming, we deal with various kinds of data: numbers for calculations, text for messages,
# and true/false values for logic. Different variable types allow the computer to know how much
# memory to allocate and what operations are valid for that data (e.g., you can multiply two
# integers, but multiplying two strings doesn't usually make sense).
# Types also help prevent errors by ensuring data is used correctly.

# Example 1: Basic variables and types
# Variables in Python are dynamically typed. You don't need to specify the type.
name = "Alice"       # String (str)
age = 30             # Integer (int)
height = 5.7         # Float (float)
is_student = False   # Boolean (bool)

# Example 2: Type conversion (Casting)
# You can easily convert one data type to another
number_string = "100"
converted_int = int(number_string)  # Converts string "100" to integer 100
float_version = float(converted_int)  # Converts integer 100 to float 100.0

# Example 3: String formatting
# F-strings provide a concise way to embed expressions inside string literals
item = "apple"
price = 1.50
# The variables inside {} will be evaluated and inserted into the string
receipt = f"The price of one {item} is ${price:.2f}" 

# ------------------------------------------
# 2. CONDITIONALS (Decision Making)
# ------------------------------------------
# THEORY:
# Why do we use conditional statements?
# Conditionals allow our programs to make decisions and execute different code paths based on specific
# conditions. Without them, a program would just run top-to-bottom performing the exact same
# steps every time. Conditionals enable logic like "if the user is logged in, show their profile;
# otherwise, show the login screen."

# Example 1: Basic if-else statement
# Checks a condition and executes the block if True, otherwise executes the else block
temperature = 25
if temperature > 30:
    print("It's a hot day.")
else:
    print("It's not too hot.")

# Example 2: if-elif-else chain
# Used to check multiple conditions sequentially
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'

# Example 3: Ternary operator (Inline if-else)
# A shorter way to write a simple if-else statement in one line
age = 20
# Value becomes "Adult" if age >= 18, otherwise "Minor"
status = "Adult" if age >= 18 else "Minor"

# ------------------------------------------
# 3. LOOPS (Iteration)
# ------------------------------------------
# THEORY:
# Why do we use loops?
# Loops are used to repeat a block of code multiple times without manually duplicating the code.
# They are essential for processing collections of data (like a list of items), continuously 
# running a program (like a game loop), or automating repetitive tasks, thereby saving time 
# and reducing human error.

# Example 1: For loop over a sequence
# Iterates over elements of a sequence (like a list, string, or range)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    # This block executes once for each fruit in the list
    print(f"I like {fruit}")

# Example 2: For loop with range()
# The range() function generates a sequence of numbers. 
# range(5) generates numbers from 0 to 4 (5 is exclusive).
for i in range(5):
    print(f"Current count: {i}")

# Example 3: While loop
# Keeps executing the block as long as the condition remains True
count = 3
while count > 0:
    print(f"Countdown: {count}")
    # It's crucial to update the variable used in the condition to avoid an infinite loop
    count -= 1 

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

# Example 2: Function with default parameter values
# If an argument is not provided when calling the function, it uses the default value.
def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Example 3: Function with variable number of arguments (*args and **kwargs)
# *args allows passing a variable number of positional arguments (as a tuple)
# **kwargs allows passing a variable number of keyword arguments (as a dictionary)
def process_data(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

# ------------------------------------------
# 5. INPUTS
# ------------------------------------------
# THEORY:
# Why do we use inputs?
# Inputs allow our programs to be interactive and dynamic rather than static. By accepting data from 
# the user (like their name, age, or a command), the program can produce different outputs 
# and behaviors for different users. It is the core of how users interact with software.

# Example 1: Basic string input
# The input() function pauses the program and waits for the user to type something and press Enter.
# Note: These examples are commented out so they don't block the script execution.
# user_name = input("Please enter your name: ")
# print(f"Hello, {user_name}!")

# Example 2: Input with type conversion
# input() always returns a string, so we must convert it if we need numbers.
# age_input = input("Enter your age: ")
# age_int = int(age_input)
# print(f"Next year you will be {age_int + 1}")

# Example 3: Handling invalid inputs safely
# It's good practice to handle cases where the user inputs the wrong type of data.
# try:
#     number_input = input("Enter a whole number: ")
#     number = int(number_input)
#     print(f"You entered: {number}")
# except ValueError:
#     print("That wasn't a valid whole number!")

# ------------------------------------------
# 6. DATA STRUCTURES (Lists and Dictionaries)
# ------------------------------------------

# Example 1: Working with Lists (Ordered, mutable sequences)
# Lists can hold different types of items and can be modified after creation.
numbers = [1, 2, 3, 4, 5]
numbers.append(6)      # Adds 6 to the end
first_item = numbers[0] # Accesses the first element (index is 0-based)
numbers[1] = 20        # Changes the second element to 20

# Example 2: List Comprehensions
# A concise way to create new lists based on existing iterables
squares = [x**2 for x in range(1, 6)] # Creates [1, 4, 9, 16, 25]
even_squares = [x**2 for x in range(1, 6) if x % 2 == 0] # Creates [4, 16]

# Example 3: Working with Dictionaries (Key-Value pairs)
# Dictionaries store data in key-value pairs and are optimized for retrieving values by key.
person = {
    "name": "Bob",
    "age": 25,
    "city": "New York"
}
# Accessing the value associated with the key "name"
person_name = person["name"] 
# Adding a new key-value pair
person["job"] = "Engineer"   

# ------------------------------------------
# 7. EXCEPTION HANDLING (Errors)
# ------------------------------------------

# Example 1: Basic try-except block
# Used to handle potential runtime errors gracefully without crashing the program
try:
    result = 10 / 0 # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # This block executes if the specific error occurs
    print("Error: Cannot divide by zero!")

# Example 2: Catching multiple exceptions
# You can handle different types of errors differently
try:
    number = int("abc") # This will raise a ValueError
except ValueError:
    print("Error: Invalid invalid string for integer conversion.")
except TypeError:
    print("Error: Invalid type provided.")

# Example 3: try-except-finally
# The 'finally' block always executes, regardless of whether an exception occurred or not.
# It's commonly used for cleanup operations (like closing files).
try:
    value = 10 / 2
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Execution finished. This prints no matter what.")

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
