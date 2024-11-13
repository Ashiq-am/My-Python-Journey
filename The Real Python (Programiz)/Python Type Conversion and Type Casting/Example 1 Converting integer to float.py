num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))
print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))



#In the above program,

#We add two variables num_int and num_flo, storing the value in num_new.
# We will look at the data type of all three objects respectively.
# In the output we can see the datatype of num_int is an integer, datatype of num_flo is a float.
# Also, we can see the num_new has float data type because Python always converts smaller data type to larger data type to avoid the loss of data.