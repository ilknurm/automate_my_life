# Write a code to return True if the list’s first and last numbers are the same. 
# If the numbers are different, return False.

import random

a = [random.randint(1,5) for _ in range(3)]

print(a)

if a[0] == a[-1]:
    print(True)
    
else:
    print(False)