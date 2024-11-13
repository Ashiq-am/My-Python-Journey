from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Male'

man = Man.fromBirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.fromFathersAge('John', 1965, 20)
print(isinstance(man1, Man))















#Here, using a static method to create a class instance wants us to hardcode the instance type during creation.

#This clearly causes a problem when inheriting Person to Man.

#fromFathersAge method doesn't return a Man object but its base class Person's object.

#This violates OOP paradigm. Using a class method as fromBirthYear can ensure the OOP-ness of the code since
# it takes the first parameter as the class itself and calls its factory method.