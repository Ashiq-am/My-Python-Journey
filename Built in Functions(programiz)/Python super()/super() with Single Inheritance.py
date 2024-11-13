class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')


class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        super().__init__('Dog')


d1 = Dog()









#Method Resolution Order (MRO) is the order in which methods should be inherited in the presence of multiple inheritance. You can view the MRO by using the __mro__ attribute.

#>>> Dog.__mro__
# (<class 'Dog'>,
# <class 'NonMarineMammal'>,
# <class 'NonWingedMammal'>,
# <class 'Mammal'>,
# <class 'Animal'>,
# <class 'object'>)

#Here is how MRO works:

#A method in the derived calls is always called before the method of the base class.

#In our example, Dog class is called before NonMarineMammal or NoneWingedMammal.

#These two classes are called before Mammal, which is called before Animal, and Animal class is called before the object.

#If there are multiple parents like Dog(NonMarineMammal, NonWingedMammal),
#methods of NonMarineMammal is invoked first because it appears first.









# changing base class to CanidaeFamily
class Dog(CanidaeFamily):
  def __init__(self):
    print('Dog has four legs.')

    # no need to change this
    super().__init__('Dog')







#The super() builtin returns a proxy object, a substitute object that can call methods of the base class via delegation.
# This is called indirection (ability to reference base object with super())

#Since the indirection is computed at the runtime, we can use different base classes at different times (if we need to).