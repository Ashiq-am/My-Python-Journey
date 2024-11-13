def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    printer()

# We execute the function
# Output: Hello
print_msg("Hello")



#We can see that the nested function printer() was able to access the non-local variable msg of the enclosing function.