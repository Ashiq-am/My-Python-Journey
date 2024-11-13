o1 = type('X', (object,), dict(a='Foo', b=12))
print(type(o1))
print(vars(o1))


class test:
    a = 'Foo'
    b = 12


o2 = type('Y', (test,), dict(a='Foo', b=12))
print(type(o2))
print(vars(o2))













#In the program, we have used the Python vars() function which returns the __dict__ attribute. __dict__ is used
# to store object's writable attributes.

#You can easily change these attributes if necessary.
# For example, if you need to change the __name__ attribute of o1 to 'Z', use:

#o1.__name = 'Z'