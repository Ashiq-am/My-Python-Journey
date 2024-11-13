# first string
firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "abcdef"
print("Original string:", string)

translation = string.maketrans(firstString, secondString, thirdString)

# translate string
print("Translated string:", string.translate(translation))









#Here, the translation mapping translation contains the mapping from a, b and c to g, h and i respectively.

#But, the removal string thirdString resets the mapping to a and b to None.

#So, when the string is translated using translate(), a and b are removed, and c is replaced i outputting idef.