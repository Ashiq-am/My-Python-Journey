# Note: You may get different value of id

a = 2
# Output: id(2)= 10919424
print('id(2) =', id(2))

# Output: id(a) = 10919424
print('id(a) =', id(a))











#Here, both refer to the same object. Let's make things a little more interesting.









# Note: You may get different value of id

a = 2

# Output: id(a) = 10919424
print('id(a) =', id(a))

a = a+1

# Output: id(a) = 10919456
print('id(a) =', id(a))

# Output: id(3) = 10919456
print('id(3) =', id(3))

b = 2

# Output: id(2)= 10919424
print('id(2) =', id(2))














def printHello():
    print("Hello")
a = printHello()

# Output: Hello

a





#Our same name a can refer to a function and we can call the function through it, pretty neat.