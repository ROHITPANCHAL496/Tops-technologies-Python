# Write a Python program to check if a number is positive, negative or zero.  

num = float(input("Enter number: "))
if num > 0:
    print(f"{num} Number is positive")
elif num < 0:
    print(f"{num} Number is negative")
else:
    print(f"{num} Number is Zero")
