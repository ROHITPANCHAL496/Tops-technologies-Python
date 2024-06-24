# Write a Python program to get the Factorial number of given number.
f = 1
num = float(input("Enter your number: "))
num = int(num)
for fact in range(1, num + 1):
            f *= fact
print(f"Factorial of {num} is {f}")
