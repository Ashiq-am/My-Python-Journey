x = "global"

def foo():
    print("x inside :", x)

foo()
print("x outside:", x)




#When we run the code, the will output be:

#x inside : global
#x outside: global

#In above code, we created x as a global variable and defined a foo() to print the global variable x.
# Finally, we call the foo() which will print the value of x.

#What if you want to change value of x inside a function?

x = "global"

def foo():
    x = x * 2
    print(x)
foo()



#When we run the code, the will output be:

#UnboundLocalError: local variable 'x' referenced before assignment

#The output shows an error because Python treats x as a local variable and x is also not defined inside foo().