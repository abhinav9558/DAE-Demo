
name = "Abhinav"       # String (str)
age = 26            # Integer (int)
height = 5234567876543.115555       # Float (float)
bank_account = 1234567876543.115555       # Float (float)
is_student = False   # Boolean (bool)
print(f"My account balance is: ${bank_account:,.1f}")

# print(f"Name: {name}, Age: {age}, Height: ${height:,.2f}, Student: {is_student}")
#print("Name:", name, "Age:", age, "Height:", height, "Student:", is_student)



# # Example 2: Type conversion (Casting)
# # You can easily convert one data type to another
# number_string = "100"
# converted_int = int(number_string)  # Converts string "100" to integer 100
# float_version = float(converted_int)  # Converts integer 100 to float 100.0
# print(f"String: '{number_string}', Int: {converted_int}, Float: {float_version}")

# # Example 3: String formatting
# # F-strings provide a concise way to embed expressions inside string literals
# item = "apple"
# price = 1.50
# # The variables inside {} will be evaluated and inserted into the string
# receipt = f"The price of one {item} is ${price:.2f}" 
# print(receipt)
