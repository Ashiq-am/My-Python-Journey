# Function to find HCF the Using Euclidian algorithm
def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = compute_hcf(300, 400)
print("The HCF is", hcf)




'''This algorithm is based on the fact that H.C.F. of two numbers divides their difference as well.

In this algorithm, we divide the greater by smaller and take the remainder. 
Now, divide the smaller by this remainder. Repeat until the remainder is 0.

For example, if we want to find the H.C.F. of 54 and 24, we divide 54 by 24. 
The remainder is 6. Now, we divide 24 by 6 and the remainder is 0. Hence, 6 is the required H.C.F.'''






'''Here we loop until y becomes zero. The statement x, y = y, x % y does swapping of values in Python. 
Click here to learn more about swapping variables in Python.

In each iteration, we place the value of y in x and the remainder (x % y) in y, simultaneously. 
When y becomes zero, we have H.C.F. in x.'''