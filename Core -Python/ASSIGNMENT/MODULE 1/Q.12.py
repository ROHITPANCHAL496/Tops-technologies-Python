# Write a Python program to test whether a passed letter is a vowel or 
# not.  
v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
letter = input("Enter a letter: ")
if letter in v:
    print("The letter is a vowel.")
else:
    print("The letter is not a vowel.")