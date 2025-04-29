# Exercise 1:
# Write a program that will ask the user to enter three numbers and then return the sum
a= float(input("Please enter a number: "))
b= float(input("Please enter another number: "))
c= float(input("Please enter a final number :"))
print(a+b+c)

#Exercise 2: Ask the user to input 2 numbers and then perform the following mathematical operation on those two 
# numbers: +, -, *, /, %, //, **. For each operation print out the operation name and the result.

a=float(input("Enter a number: "))
b=float(input("Enter a second number: "))

mod=a % b
print(f"{mod} This is modulus")

# Exercise 3: What will be the result of the following python operations?
# 0 / 4
# 4 / 0

print(0/4)
print(4/0)

# # # Exercise 4: Correct these lines of code using type conversion. Then print the calculated result of all three variables and their data type.
# # # price_3_books = '5.0' * 3
# # # my_age = 'I am ' + 26
# # # total_bill = 4.45 + 3.30 + 6 + '7'

price_3_books = int(float('5.0')) * 3
my_age = 'I am ' + str(26)
total_bill = 4.45 + 3.30 + 6 + int('7')

print(f"{price_3_books} This i a float") 
print(f"{my_age} This is  a string")
print(f"{total_bill} This is an int")


# Exercise 5:
# Suppose your teacher wants to calculate your average grade, based on three grades that it gave you for an assignment. 
# Ask the user three times to input a number (assignment grade, convert the input to the correct data type and assign them 
# to variables.
# Calculate and print the average of the three numbers. Provide your code with useful comments.

a=float(input("What is your first grade? "))
b=float(input("What is your second grade? "))
c=float(input("What is your third grade? "))

average = (a+b+c)/3
print(f"{average} This is your average")
