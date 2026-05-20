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
