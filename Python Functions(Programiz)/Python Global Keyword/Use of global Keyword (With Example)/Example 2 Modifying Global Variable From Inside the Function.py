c = 1  # global variable


def add():
    c = c + 2  # increment c by 2
    print(c)


add()



#When we run above program, the output shows an error:

#UnboundLocalError: local variable 'c' referenced before assignment

#This is because we can only access the global variable but cannot modify it from inside the function.

#The solution for this is to use the global keyword.