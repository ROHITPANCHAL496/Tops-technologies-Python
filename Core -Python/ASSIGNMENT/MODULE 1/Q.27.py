# Write a Python function to insert a string in the middle of a string.  
str1= "python"
str2=input("enter string ")
v=len(str1)
m=v//2
new_str1= str1[:m] + str2 + str1[m:]
print(new_str1)