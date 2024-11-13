# example dictionary
dict = {"a": "123", "b": "456", "c": "789"}
string = "abc"
print(string.maketrans(dict))

# example dictionary
dict = {97: "123", 98: "456", 99: "789"}
string = "abc"
print(string.maketrans(dict))







#Here, a dictionary dict is defined. It contains a mapping of characters a,b and c to 123, 456 and 789 respectively.

#maketrans() creates a mapping of the character's Unicode ordinal to its corresponding translation.

#So, 97 ('a') is mapped to '123', 98 'b' to 456 and 99 'c' to 789. This can be demonstrated from the output of both dictionaries.