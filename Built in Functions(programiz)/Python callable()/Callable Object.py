class Foo:
  def __call__(self):
    print('Print Something')

print(callable(Foo))





#The instance of Foo class appears to be callable (and is callable in this case).




class Foo:
  def __call__(self):
    print('Print Something')

InstanceOfFoo = Foo()

# Prints 'Print Something'
InstanceOfFoo()