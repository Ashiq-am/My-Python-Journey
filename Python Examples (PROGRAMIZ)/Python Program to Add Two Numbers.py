# This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))







'''Source Code: Add Two Numbers Provided by The User'''



# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))




"""In this program, we asked the user to enter two numbers and this program displays the sum of two numbers entered by user.

We use the built-in function input() to take the input. input() returns a string, 
so we convert it into number using the float() function.

Alternative to this, we can perform this addition in a single statement without using any variables as follows."""




print('The sum is %.1f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))