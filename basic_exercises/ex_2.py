# Write Python code to iterate through the first 10 numbers and, in each iteration, 
# print the sum of the current and previous number.

previous_sum = 0 
for x in range(1,11):
    new_sum = previous_sum + x
    print(f"The previous sum is {previous_sum} and the new sum is {new_sum}")
    previous_sum = new_sum