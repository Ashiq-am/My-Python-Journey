# define Person dictionary
person = {'age': 23, 'name': 'Adam'}

# format age
print("{p[name]}'s age is: {p[age]}".format(p=person))






#There's an easier way to format dictionaries in Python using str.format(**mapping).











# define Person dictionary
person = {'age': 23, 'name': 'Adam'}

# format age
print("{name}'s age is: {age}".format(**person))