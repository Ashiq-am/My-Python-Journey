"""The factorial of a number is the product of all the integers from 1 to that number.

For example, the factorial of 6 is 1*2*3*4*5*6 = 720.

Factorial is not defined for negative numbers, and the factorial of zero is one, 0! = 1."""





# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)






"""Note: To test the program for a different number, change the value of num.

Here, the number whose factorial is to be found is stored in num, 
and we check if the number is negative, zero or positive using if...elif...else statement. 
If the number is positive, we use for loop and range() function to calculate the factorial."""