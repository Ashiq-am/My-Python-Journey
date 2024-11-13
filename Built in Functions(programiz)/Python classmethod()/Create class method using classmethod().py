class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)

# create printAge class method
Person.printAge = classmethod(Person.printAge)

Person.printAge()








#Here, we have a class Person, with a member variable age assigned to 25.

#We also have a function printAge which takes a single parameter cls and not self we usually take.

#cls accepts the class Person as a parameter rather than Person's object/instance.

#Now, we pass the method Person.printAge as an argument to the function classmethod.
#This converts the method to a class method so that it accepts the first parameter as a class (i.e. Person).

#In the final line, we call printAge without creating a Person object like we do for static methods. This prints the class variable age.