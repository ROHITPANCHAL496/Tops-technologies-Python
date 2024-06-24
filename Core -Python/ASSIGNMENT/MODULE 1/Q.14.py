#  Write a Python program that will return true if the two given integer 
# values are equal or their sum or difference is 5.  
num1 = int(input("Enter an Int1: "))
num2 = int(input("Enter an Int2: "))
num3 = 5
if num1 == num2 or num1 + num2 == num3 or num1 - num2 == num3:  
    print("true")
else:
    print("false")