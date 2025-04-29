# Given two integer numbers, write a Python program to return their product only 
# if the product is equal to or lower than 1000. Otherwise, return their sum.

#a = int(input("Enter any number between 1 and 1000: "))

#b = int(input("Enter any number between 1 and 1000: "))

#c = a * b

#if a * b <= 1000:
#    print(c)
#else:
#    print(a+b)

import random
a=random.randint(1,1000)
b=random.randint(1,1000)

print(a)
print(b)
c = a*b 

if c >= 600:
    print(c)
else:
    print(a+b)