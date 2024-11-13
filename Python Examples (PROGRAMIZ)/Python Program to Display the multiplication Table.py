'''In the program below, we have used the for loop to display the multiplication table of 12.'''


# Multiplication table (from 1 to 10) in Python

num = 12

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)













"""Here, we have used the for loop along with the range() function to iterate 10 times. 
The arguments inside the range() function are (1, 11). Meaning, greater than or equal to 1 and less than 11.

We have displayed the multiplication table of variable num (which is 12 in our case). 
You can change the value of num in the above program to test for other values."""