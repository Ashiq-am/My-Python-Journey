from math import *
print(eval('dir()', {'sqrt': sqrt, 'pow': pow}))










from math import *
print(eval('dir()', {'squareRoot': sqrt, 'pow': pow}))

# Using squareRoot in Expression
print(eval('squareRoot(9)', {'squareRoot': sqrt, 'pow': pow}))