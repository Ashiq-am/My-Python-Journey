# translation table - a dictionary
translation = {97: None, 98: None, 99: 105}

string = "abcdef"
print("Original string:", string)

# translate string
print("Translated string:", string.translate(translation))








#Here, we don't create a translation table from maketrans() but, we manually create the mapping dictionary translation.

#This translation is then used to translate the string string to get the same output as the previous example.