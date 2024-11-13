str = 'root33'
if str.isidentifier() == True:
    print(str, 'is a valid identifier.')
else:
    print(str, 'is not a valid identifier.')

str = '33root'
if str.isidentifier() == True:
    print(str, 'is a valid identifier.')
else:
    print(str, 'is not a valid identifier.')

str = 'root 33'
if str.isidentifier() == True:
    print(str, 'is a valid identifier.')
else:
    print(str, 'is not a valid identifier.')