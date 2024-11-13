class Quantity:
    apple = 1
    orange = 2
    grapes = 2

    def __index__(self):
        return self.apple + self.orange + self.grapes


print('The binary equivalent of quantity is:', bin(Quantity()))






#Here, we've sent an object of class Quantity to the bin() method.

#The bin() method doesn't raise an error even if the object Quantity is not an integer.

#This is because, we have implemented the __index__() method which returns an integer (sum of fruit quantities).
# This integer is then supplied to the bin() method.