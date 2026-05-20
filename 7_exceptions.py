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
    print("Error: Invalid string for integer conversion.")
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
