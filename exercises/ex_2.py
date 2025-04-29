# Exercise 6: String Concatenation
# Create two variables first_name and last_name and assign them your first and last names.
# Print your full name using string concatenation.

first_name= "Nurbuntu" 
last_name= "Manav"
#fstring
print(f"{first_name} {last_name}") 

#format method
full_name="Your name is: {} {}".format(first_name,last_name)
print(full_name)

# join method
full_name = " ".join([first_name,last_name])
print(full_name)

full_name = first_name +" " + last_name
print(f"Your name is {full_name}")

# Exercise 7: Type Conversion
# Given the string num_str = "42" and the integer factor = 3.
# Convert num_str to an integer and calculate its product with factor.Print the result.

num_string=int("42")
factor=3

sum = num_string + factor
print(sum)



# Exercise 8: Combining Strings and Numbers
# Create a variable age and assign it your age as an integer.
# Create a variable message that says: "I am X years old." Replace X with the value of age.
# Print the message.

age=int(33)
message=(f"Iam {age} years old")
print(message)

# Exercise 9: Variables and Basic Arithmetic
# Create two variables num1 and num2 and assign them any integer values.
# Print the sum, difference, product, and quotient of num1 and num2.

num_1 = 5
num_2 = 10 
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 / num_2)
print(num_1 * num_2)
# Exercise 10: Working with Floats
# Ask the user to enter the radius of a circle (use input()).
# Convert the input to a float and calculate the area of the circle
# (Area = (π * radius * radius)).
# π is the constant pi (3.14159).Print the area.

radius = float(input("What is the radius of a circle? "))
pi = 3.14
area= pi * radius * radius
print(area)