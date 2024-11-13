x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)





#Here, 'H' is in x but 'hello' is not present in x (remember, Python is case sensitive).
# Similary, 1 is key and 'a' is the value in dictionary y. Hence, 'a' in y returns False.