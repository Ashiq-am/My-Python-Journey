string = 'THIS IS GOOD'
if string.isupper() == True:
    print('Does not contain lowercase letter.')
else:
    print('Contains lowercase letter.')

string = 'THIS IS gOOD'
if string.isupper() == True:
    print('Does not contain lowercase letter.')
else:
    print('Contains lowercase letter.')