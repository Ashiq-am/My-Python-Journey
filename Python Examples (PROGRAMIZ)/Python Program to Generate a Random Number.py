# Program to generate a random number between 0 and 9

# importing the random module
import random

print(random.randint(0,50000000))



'''To generate random number in Python, randint() function is used. This function is defined in random module.'''






"""Note that we may get different output because this program generates random number in range 0 and 9. 
The syntax of this function is:

random.randint(a,b)


This returns a number N in the inclusive range [a,b], meaning a <= N <= b, where the endpoints are included in the range."""