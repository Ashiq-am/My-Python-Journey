from math import *

a = 5
print(eval('sqrt(a)', {'__builtins__': None}, {'a': a, 'sqrt': sqrt}))