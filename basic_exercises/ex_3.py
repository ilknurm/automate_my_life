# Write a Python code to accept a string from the user and display characters 
#present at an even index number.
# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

x = input("Enter a random string: ")

for index, char in enumerate(x):
    if index % 2 == 0:
        print(char)