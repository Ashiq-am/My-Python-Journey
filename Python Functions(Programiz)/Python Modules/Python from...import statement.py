#We can import specific names from a module without importing the module as a whole. Here is an example.

# import only pi from math module

from math import pi
print("The value of pi is", pi)






#We imported only the attribute pi from the module.

#In such case we don't use the dot operator. We could have imported multiple attributes as follows.

#>>> from math import pi, e
# >>> pi
# 3.141592653589793
# >>> e
# 2.718281828459045