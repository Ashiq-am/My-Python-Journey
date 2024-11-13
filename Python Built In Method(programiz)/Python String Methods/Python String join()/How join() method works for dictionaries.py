test =  {'mat': 1, 'that': 2}
s = '->'
print(s.join(test))

test =  {1:'mat', 2:'that'}
s = ', '

# this gives error
print(s.join(test))