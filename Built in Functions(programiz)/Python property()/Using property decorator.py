class Person:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        print('Getting name')
        return self._name
    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value
    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name
p = Person('Adam')
print('The name is:', p.name)
p.name = 'John'
del p.name


















#Here, instead of using property(), we've used the @property decorator.

#First, we specify that name() method is also an attribute of Person.
# This is done by using @property before the getter method as shown in the program.

#Next, we use the attribute name to specify the setter and the deleter.

#This is done by using @name.setter for the setter method and @name.deleter for the deleter method.

#Notice, we've used the same method name() with different definitions for defining the getter, setter, and deleter.

#Now, whenever we use p.name, it internally calls the appropriate getter, setter,
# and deleter as shown by the printed output present inside the method.