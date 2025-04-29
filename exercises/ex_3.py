# Exercise 11: Combining Strings and Operators
# Ask the user to enter their name (use input()).
# Create a welcome message with their name using string concatenation (e.g., "Welcome, John!"). Print the welcome message.

#name = input("What is your name? ")
#greeting = "Welcome"
#print("Welcome" + " "+ name )

#message = " ".join([greeting,name])
#print(message)

#message = "{} {}".format(greeting,name)
#print(message)


# Exercise 12: User Input and Arithmetic
# Ask the user to enter two numbers (use input() to receive input).
# Convert the input strings to integers and assign them to variables.
# Calculate and print the sum and product of the two numbers.

#a = int(input("Enter a  number: "))
#b = int(input("Enter a second number: "))

#sum = a + b
#product = a * b
#print(sum)
#print(product)

# Exercise 13: Temperature Conversion
# Ask the user to enter a temperature in Celsius (use input()).
# Convert the input to a float and calculate the temperature in Fahrenheit (F = C * 9/5 + 32).
# Print the temperature in Fahrenheit.

#temp = float(input("Enter a temperature in celcius: "))
#temp_fahrenheit = temp * 9/5 + 32
#print(temp_fahrenheit)

# Exercise 14: Length of String
# Ask the user to enter a word or a sentence using input().
# Calculate and print the length of the input string.

#a = input("Enter a word:")
#length = len(a)
#print("Your word is" + " "+ str(length)+ " "+ "characters")

# Exercise 15: Integer Division and Remainder
# Ask the user to enter two integers (numerator and denominator) using input().
# Convert the input to integers and calculate the result of integer division and the remainder. Print the quotient and remainder.

a = int(input("Enter two numbers: "))
b = int(input("Enter another number: "))

division = a // b
remainder = a%b
print(division)
print(remainder)