# Write a Python program to count the occurrences of each word in a given sentence 
from collections import Counter
quote = 'powerful people make places powerful'
freq = Counter(quote.split()).most_common()
print(str(freq) , end=" ")