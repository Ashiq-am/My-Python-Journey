c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()





#When we run above program, the output will be:

#Inside add(): 2
#In main: 2

#In the above program, we define c as a global keyword inside the add() function.
# Then, we increment the variable c by 1, i.e c = c + 2. After that, we call the add() function. Finally, we print global variable c.
# As we can see, change also occured on the global variable outside the function, c = 2.