# Write a Python program to get the Fibonacci series of given range.  
num=int(input("Enter number: "))
n1=0
n2=1
n3=0
for febonacci_series in range(num):
  print(n3,end=" ")
  n1=n2
  n2=n3
  n3=n1+n2
