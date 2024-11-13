"""And so on… This type of generator is returned by the yield statement from a function. Here is an example."""


def generator():
    for i in range(6):
        yield i*i

g = generator()
for i in g:
    print(i)




'''Here, the function generator() returns a generator that generates square of numbers from 0 to 5. This is printed in the for loop.'''