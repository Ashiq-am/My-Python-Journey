class Foo:
  def printLine(self):
    print('Print Something')

print(callable(Foo))







#The instance of Foo class appears to be callable but it's not callable. The following code will raise an error.





class Foo:
  def printLine(self):
    print('Print Something')

print(callable(Foo))

InstanceOfFoo = Foo()
# Raises an Error
# 'Foo' object is not callable
InstanceOfFoo()