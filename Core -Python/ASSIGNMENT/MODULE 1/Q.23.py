# Write a Python program to find the first appearance of the substring 
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
# whole 'not'...'poor' substring  with 'good'. Return the resulting string.

s = input("Enter a string: ")
def replace_not_poor(s):
    not_index = s.find('not')
    poor_index = s.find('poor')
    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        s = s[:not_index] + 'good' + s[poor_index + 4:]
    return s
print("Resulting string:", replace_not_poor(s))