import datetime
# datetime formatting
date = datetime.datetime.now()
print("It's now: {:%Y/%m/%d %H:%M:%S}".format(date))

# complex number formatting
complexNumber = 1+2j
print("Real part: {0.real} and Imaginary part: {0.imag}".format(complexNumber))

# custom __format__() method
class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'

print("Adam's age is: {:age}".format(Person()))









#Here,

#For datetime:
# Current datetime is passed as a positional argument to the format() method.
# And, internally using __format__() method, format() accesses the year, month, day, hour, minutes and seconds.

#For complex numbers:
# 1+2j is internally converted to a ComplexNumber object.
# Then accessing its attributes real and imag, the number is formatted.


#Overriding __format__():
# Like datetime, you can override your own __format__() method for custom formatting which returns age when accessed as {:age}