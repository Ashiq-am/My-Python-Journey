# first string
firstString = "abc"
secondString = "def"
thirdString = "abd"
string = "abc"
print(string.maketrans(firstString, secondString, thirdString))











#Here, first the mapping between the two strings firstString and secondString are created.

#Then, the third argument thirdString resets the mapping of each character in it to None and also creates new mapping for non-existent characters.

#In this case, thirdString resets the mapping of 97 ('a') and 98 ('b') to None, and also creates a new mapping for 100 ('d') mapped to None.