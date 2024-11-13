#When we are done with operations to the file, we need to properly close the file.
# Closing a file will free up the resources that were tied with the file and is done using Python close() method.
# Python has a garbage collector to clean up unreferenced objects but, we must not rely on it to close the file.


f = open("test.txt",encoding = 'utf-8')
# perform file operations
f.close()




#This method is not entirely safe. If an exception occurs when we are performing some operation with the file,
# the code exits without closing the file.
# A safer way is to use a try...finally block.


try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()





#The best way to do this is using the with statement.
# This ensures that the file is closed when the block inside with is exited.

#We don't need to explicitly call the close() method. It is done internally.

with open("test.txt", encoding ='utf-8') as f:
# perform file operations






