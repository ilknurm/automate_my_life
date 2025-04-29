#Write a Python code to display numbers from a list divisible by 5

import random

a = [random.randint(1,100) for _ in range(5)]
print(a)

for x in a:
    if x % 5 == 0:
        print(x)

