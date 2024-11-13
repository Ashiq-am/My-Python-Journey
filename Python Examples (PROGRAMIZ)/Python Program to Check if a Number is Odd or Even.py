"""A number is even if it is perfectly divisible by 2. When the number is divided by 2,
we use the remainder operator % to compute the remainder.

If the remainder is not zero, the number is odd."""






# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))




'''In this program, we ask the user for the input and check if the number is odd or even.'''



