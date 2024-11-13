x = 5
print(callable(x))

def testFunction():
  print("Test")

y = testFunction
print(callable(y))







#Here, the object x is not callable. And, the object y appears to be callable (but may not be callable).