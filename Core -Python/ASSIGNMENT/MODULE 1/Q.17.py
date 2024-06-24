# Write a Python program to count the number of characters (character frequency) in a string 
students_name = ['rohit', 'arvind', 'deepak', 'kuldeep','ramesh','lokesh', 'deepak','kuldeep','lipi','ramesh','arvind','rohit','deepak','kuldeep']
s_count = input("Enter a word: ")
count = 0
for name in students_name:
    if name == s_count:
        count += 1
print(f"'{s_count}'  {count} times in the list.")