# Python program to find the L.C.M. of two input number

# This function computes GCD
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))




'''The output of this program is the same as before. 
We have two functions compute_gcd() and compute_lcm(). We require G.C.D. of the numbers to calculate its L.C.M.

So, compute_lcm() calls the function compute_gcd() to accomplish this. G.C.D. of 
two numbers can be calculated efficiently using the Euclidean algorithm.'''