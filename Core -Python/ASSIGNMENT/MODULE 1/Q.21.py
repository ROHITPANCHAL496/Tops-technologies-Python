#  Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string. 
# Get the input strings
str1 = input("Enter first string: ")   
str2 = input("Enter second string: ")  

new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

str3 = new_str1 + ' ' + new_str2

print(str3)
