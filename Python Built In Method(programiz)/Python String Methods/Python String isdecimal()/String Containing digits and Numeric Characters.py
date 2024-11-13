s = '23455'
print(s.isdecimal())

#s = '²3455'
s = '\u00B23455'
print(s.isdecimal())

# s = '½'
s = '\u00BD'
print(s.isdecimal())