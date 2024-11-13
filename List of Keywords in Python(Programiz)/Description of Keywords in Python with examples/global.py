globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar = 5
def write2():
    globvar = 15

read1()
write1()
read1()
write2()
read1()



'''Here, the read1() function is just reading the value of globvar. So, we do not need to declare it as global. 
But the write1() function is modifying the value, so we need to declare the variable as global.

We can see in our output that the modification did take place (10 is changed to 5). The write2() also tries to modify this value. 
But we have not declared it as global.

Hence, a new local variable globvar is created which is not visible outside this function.
Although we modify this local variable to 15, 

the global variable remains unchanged. This is clearly visible in our output.'''