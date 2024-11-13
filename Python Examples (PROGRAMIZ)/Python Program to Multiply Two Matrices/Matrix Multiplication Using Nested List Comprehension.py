# Program to multiply two matrices using list comprehension

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

# result is 3x4
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
   print(r)





"""The output of this program is the same as above. To understand the above code we must first 
know about built-in function zip() and unpacking argument list using * operator.

We have used nested list comprehension to iterate through each element in the matrix.
The code looks complicated and unreadable at first. But once you get the hang of list comprehensions, 
you will probably not go back to nested loops."""