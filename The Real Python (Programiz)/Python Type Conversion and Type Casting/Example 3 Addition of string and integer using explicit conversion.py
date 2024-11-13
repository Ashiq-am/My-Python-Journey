num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))










#In above program,
# We add num_str and num_int variable.
# We converted num_str from string(higher) to integer(lower) type using int() function to perform the addition.
# After converting num_str to a integer value Python is able to add these two variable.
# We got the num_sum value and daa type to be integer.







