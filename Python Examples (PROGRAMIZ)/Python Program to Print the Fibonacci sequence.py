'''A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....

The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.

This means to say the nth term is the sum of (n-1)th and (n-2)th term.'''



# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1





"""Here, we store the number of terms in nterms. We initialize the first term to 0 and the second term to 1.

If the number of terms is more than 2, we use a while loop to find the next term in the sequence by adding the preceding two terms. 
We then interchange the variables (update it) and continue on with the process."""