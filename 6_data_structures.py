# ------------------------------------------
# 6. DATA STRUCTURES (Lists and Dictionaries)
# ------------------------------------------

# Example 1: Working with Lists (Ordered, mutable sequences)
# Lists can hold different types of items and can be modified after creation.
numbers = [1, 2, 3, 4, 5]
numbers.append(6)      # Adds 6 to the end
first_item = numbers[0] # Accesses the first element (index is 0-based)
numbers[1] = 20        # Changes the second element to 20
print(f"List after modifications: {numbers}")

# Example 2: List Comprehensions
# A concise way to create new lists based on existing iterables
squares = [x**2 for x in range(1, 6)] # Creates [1, 4, 9, 16, 25]
even_squares = [x**2 for x in range(1, 6) if x % 2 == 0] # Creates [4, 16]
print(f"Squares: {squares}")
print(f"Even squares: {even_squares}")

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
print(f"Person dictionary: {person}")
