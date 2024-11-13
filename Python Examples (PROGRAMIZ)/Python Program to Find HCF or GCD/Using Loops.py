# Python program to find H.C.F of two numbers

# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = 54
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))





'''The highest common factor (H.C.F) or greatest common divisor (G.C.D) of two numbers is the largest positive 
integer that perfectly divides the two given numbers. For example, the H.C.F of 12 and 14 is 2.'''







"""Here, two integers stored in variables num1 and num2 are passed to the compute_hcf() function. 
The function computes the H.C.F. these two numbers and returns it.

In the function, we first determine the smaller of the two numbers since the H.C.F can only be 
less than or equal to the smallest number. We then use a for loop to go from 1 to that number.

In each iteration, we check if our number perfectly divides both the input numbers. 
If so, we store the number as H.C.F. At the completion of the loop, 
we end up with the largest number that perfectly divides both the numbers.

The above method is easy to understand and implement but not efficient. 
A much more efficient method to find the H.C.F. is the Euclidean algorithm."""