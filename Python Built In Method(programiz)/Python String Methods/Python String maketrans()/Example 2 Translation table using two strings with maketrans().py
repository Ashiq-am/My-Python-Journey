# first string
firstString = "abc"
secondString = "def"
string = "abc"
print(string.maketrans(firstString, secondString))

# example dictionary
firstString = "abc"
secondString = "defghi"
string = "abc"
print(string.maketrans(firstString, secondString))











#Here first, two strings of equal length "abc" and "def" are defined. And the corresponding translation is created.

#Printing only the first translation gives you a 1-to-1 mapping to each character's Unicode ordinal in firstString
# to the same indexed character on the secondString.

#In this case, 97 ('a') is mapped to 100 ('d'), 98 ('b') to 101 ('e') and 99 ('c') to 102 ('f').

#Trying to create a translation table for unequal length strings raises a ValueError exception
# indicating that the strings must have equal length.

