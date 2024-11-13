'''Example: For positive numbers'''


# Python Program to calculate the square root

# Note: change this value for a different result
num = 8

# To take the input from the user
#num = float(input('Enter a number: '))

num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))



'''In this program, we store the number in num and find the square root using the ** exponent operator. 
This program works for all positive real numbers. But for negative or complex numbers, it can be done as follows.'''









"""Source code: For real or complex numbers"""


# Find square root of real or complex numbers
# Importing the complex math module
import cmath

num = 1+2j

# To take input from the user
#num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))




"""In this program, we use the sqrt() function in the cmath (complex math) module.

Notice that we have used the eval() function instead of float() to convert complex numbers as well. 
Also, notice the way in which the output is formatted."""