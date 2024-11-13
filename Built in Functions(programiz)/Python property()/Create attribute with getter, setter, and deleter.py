class Person:
    def __init__(self, name):
        self._name = name
    def get_name(self):
        print('Getting name')
        return self._name
    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value
    def del_name(self):
        print('Deleting name')
        del self._name
    # Set property to use get_name, set_name
    # and del_name methods
    name = property(get_name, set_name, del_name, 'Name property')
p = Person('Adam')
print(p.name)
p.name = 'John'
del p.name









#Here, _name is used as the private variable for storing the name of Person.

#We also set:

#a getter method get_name() to get the name of the person,
# a setter method set_name() to set the name of the person,
# a deleter method del_name() to delete the name of the person.
# Now, we set a new property attribute name by calling the property() method.

#As shown in the program, referencing p.name internally calls get_name() as getter, set_name() as setter and del_name()
#as deleter through the printed output present inside the methods.