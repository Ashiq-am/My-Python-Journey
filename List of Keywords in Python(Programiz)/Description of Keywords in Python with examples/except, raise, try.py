def reciprocal(num):
    try:
        r = 1/num
    except:
        print('Exception caught')
        return
    return r

print(reciprocal(10))
print(reciprocal(0))



'''Here, the function reciprocal() returns the reciprocal of the input number.

When we enter 10, we get the normal output of 0.1. But when we input 0, a ZeroDivisionError is raised automatically.'''
