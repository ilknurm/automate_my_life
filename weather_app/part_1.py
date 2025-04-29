# Create a program that
# 1. asks the user to enter the name of a city and the current
# temperature in Celsius.
# 2. Store the user input in separate variables and
# 3. display them.

# PS:
# Use type conversion to ensure that the user's input for the temperature is treated as a float.


#current_city = input("Enter your current city: ")

#current_temp = float(input("What is the temperature in your city in celsius? "))

#print(f"The temperature in {current_city} is {current_temp}")



#Exercise 2:

#Now create a program that asks the user to enter the name of two cities and the current temperatures in each city in Celsius. 
#Store the user inputs in separate variables (two variables for the names and two for the temperatures) and display the average temperature.

city_1 = input("Enter the name of a city: ")
temp_1 = float(input("What is the temperature in" + " " + city_1 + ":" ))

city_2 = input("Enter a second city: ")
temp_2 = float(input("What is the temperature in" + " " + city_2 + ":"))

average = (temp_1 + temp_2)/2

temp_1_far = float(temp_1 * 9/5 + 32)
temp_2_far = float(temp_2 * 9/5 + 32)

print(average)

print(f"The temp in far in the first city is {temp_1_far}")
print(f"The temp in the second city in far is {temp_2_far}")


#Building upon exercise 2, also convert and print the average temperature in Fahrenheit. The formula for converting Celsius 
# to Fahrenheit is: 
#F = C * 9/5 + 32.


