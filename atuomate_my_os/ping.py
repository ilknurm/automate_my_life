import os 

host = input("Enter a hostname: ")

response = os.system(f"ping -c 1 {host}")

if response == 0:
    print("This host is online")
else:
    print("This host is offline")
    

