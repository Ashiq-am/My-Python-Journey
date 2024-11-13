from math import *
exec('print(dir())', {'sqrt': sqrt, 'pow': pow})

# object can have sqrt() module
exec('print(sqrt(9))', {'sqrt': sqrt, 'pow': pow})






from math import *
exec('print(dir())', {'squareRoot': sqrt, 'pow': pow})

# object can have squareRoot() module
exec('print(squareRoot(9))', {'squareRoot': sqrt, 'pow': pow})