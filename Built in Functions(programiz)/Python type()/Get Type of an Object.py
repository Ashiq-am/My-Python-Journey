numbers_list = [1, 2]
print(type(numbers_list))
numbers_dict = {1: 'one', 2: 'two'}
print(type(numbers_dict))
class Foo:
    a = 0
foo = Foo()
print(type(foo))







#If you need to check the type of an object, it is better to use the Python isinstance() function instead.
# It's because the isinstance() function also checks if the given object is an instance of the subclass.