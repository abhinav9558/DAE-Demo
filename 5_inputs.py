# ------------------------------------------
# 5. INPUTS
# ------------------------------------------
# THEORY:
# Why do we use inputs?
# Inputs allow our programs to be interactive and dynamic rather than static. By accepting data from 
# the user (like their name, age, or a command), the program can produce different outputs 
# and behaviors for different users. It is the core of how users interact with software.

print("--- Example 1: Basic string input ---")
# The input() function pauses the program and waits for the user to type something and press Enter.
user_name = input("Please enter your name: ")
print(f"Hello, {user_name}!\n")

print("--- Example 2: Input with type conversion ---")
# input() always returns a string, so we must convert it if we need numbers.
age_input = input("Enter your age: ")
age_int = int(age_input)
print(f"Next year you will be {age_int + 1}\n")

print("--- Example 3: Handling invalid inputs safely ---")
# It's good practice to handle cases where the user inputs the wrong type of data.
try:
    number_input = input("Enter a whole number: ")
    number = int(number_input)
    print(f"You entered: {number}")
except ValueError:
    print("That wasn't a valid whole number!")
