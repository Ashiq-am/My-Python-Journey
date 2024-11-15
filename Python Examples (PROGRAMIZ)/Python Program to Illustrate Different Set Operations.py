'''Python offers a datatype called set whose elements must be unique.
It can be used to perform different set operations like union, intersection, difference and symmetric difference.'''



# Program to perform different set operations like in mathematics

# define three sets
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};

# set union
print("Union of E and N is",E | N)

# set intersection
print("Intersection of E and N is",E & N)

# set difference
print("Difference of E and N is",E - N)

# set symmetric difference
print("Symmetric difference of E and N is",E ^ N)







"""In this program, we take two different sets and perform different set operations on them. 
This can equivalently done by using set methods."""