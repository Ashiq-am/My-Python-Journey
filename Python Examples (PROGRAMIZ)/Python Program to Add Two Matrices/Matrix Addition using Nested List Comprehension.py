# Program to add two matrices using list comprehension

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
   print(r)






"""The output of this program is the same as above. 
We have used nested list comprehension to iterate through each element in the matrix.

List comprehension allows us to write concise codes and we must try to use them frequently in Python. They are very helpful."""