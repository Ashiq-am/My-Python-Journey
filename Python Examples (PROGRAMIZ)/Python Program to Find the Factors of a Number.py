# Python Program to find the factors of a number

# This function computes the factor of the argument passed
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 320

print_factors(num)







'''Note: To find the factors of another number, change the value of num.

In this program, the number whose factor is to be found is stored in num, which is passed to the print_factors() function. 
This value is assigned to the variable x in print_factors().

In the function, we use the for loop to iterate from i equal to x. If x is perfectly divisible by i, it's a factor of x.'''