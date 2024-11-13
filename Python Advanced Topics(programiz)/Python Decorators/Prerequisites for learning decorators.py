def first(msg):
    print(msg)

first("Hello")

second = first
second("Hello")







def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result







#Furthermore, a function can return another function.

def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()

#Outputs "Hello"
new()


#Here, is_returned() is a nested function which is defined and returned, each time we call is_called().