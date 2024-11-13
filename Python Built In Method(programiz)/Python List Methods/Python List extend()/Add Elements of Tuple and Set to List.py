# language list
language = ['French', 'English', 'German']

# language tuple
language_tuple = ('Spanish', 'Portuguese')

# language set
language_set = {'Chinese', 'Japanese'}

# appending element of language tuple
language.extend(language_tuple)

print('New Language List: ', language)

# appending element of language set
language.extend(language_set)

print('Newest Language List: ', language)









#You can also add items of a list to another list using + or += operator. For example,

a = [1, 2]
b = [3, 4]

a += b

# Output: a = [1, 2, 3, 4]
print('a = ', a)