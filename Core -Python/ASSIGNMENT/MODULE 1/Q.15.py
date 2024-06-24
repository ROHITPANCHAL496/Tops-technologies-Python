# Write a python program to sum of the first n positive integers.
num = int(input("Enter a number: "))
num1 = 0
t_sum = 0

while num1 < num:
    num1 += 1
    t_sum += num1
    if num1 < num:
        print(num1, "+", end=" ")
    else:
        print(num1)

print("Sum of the first",num,"positive integers:", t_sum)