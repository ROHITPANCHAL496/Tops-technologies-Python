# Write a Python function that takes a list of words and returns the length 
# of the longest one. 
words = ['apple', 'ear', 'inkpot', 'orange', 'use', 'Aeroplane', 'Employee', 'Important', 'Own', 'Unique']
mx_length = 0
for word in words:  
    word_length = len(word) 
    if word_length > mx_length: 
        mx_length = word_length 
print(mx_length) 
