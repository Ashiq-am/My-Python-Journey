from math import *
exec('print(dir())', {})

# This code will raise an exception
# exec('print(sqrt(9))', {})










#If you pass an empty dictionary as globals, only the __builtins__ are available to the object (first parameter to the exec()).
#Even though we have imported math module in the above program,
# trying to access any of the functions provided by the math module will raise an exception.

#When you run the program, the output will be:

#['__builtins__']





from math import *
exec('print(dir())', {'sqrt': sqrt, 'pow': pow})

# object can have sqrt() module
exec('print(sqrt(9))', {'sqrt': sqrt, 'pow': pow})




#Here, the code that is executed by exec() can also have sqrt() and pow() methods along with __builtins__.

#It's possible to change the name of the method according to your wish.














from math import *
exec('print(dir())', {'squareRoot': sqrt, 'pow': pow})

# object can have squareRoot() module
exec('print(squareRoot(9))', {'squareRoot': sqrt, 'pow': pow})



#In the above program, squareRoot() calculates the square root (similar functionality like sqrt()).
# However, trying to use sqrt() will raise an exception.

#Restricting the Use of built-ins
#You can restrict the use of __builtins__ by giving value None to the '__builtins__' in the globals dictionary.

#exec(object, {'__builtins__': None})