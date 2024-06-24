# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

num1 = int(input("Enter an Int1: "))
num2 = int(input("Enter an Int2: "))
num3 = int(input("Enter an Int3: ")) 

if num1 == num2 or num1 == num3 or num2 == num3:
    add = 0  
else:
    add = num1 + num2 + num3 

print("Sum of Three Integers:", add)