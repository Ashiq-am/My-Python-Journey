numbers = [2.5, 3, 4, -5]
# start parameter is not provided
numbers_sum = sum(numbers)
print(numbers_sum)
# start = 10
numbers_sum = sum(numbers, 10)
print(numbers_sum)








#If you need to add floating-point numbers with exact precision, then you should use math.fsum(iterable) instead.

#If you need to concatenate items of the given iterable (items must be strings), then you can use the join() method.

#'string'.join(sequence)