#List are mutable, meaning, their elements can be changed unlike string or tuple.

#We can use assignment operator (=) to change an item or a range of items.



# mistake values
odd = [2, 4, 6, 8]

# change the 1st item
odd[0] = 1

# Output: [1, 4, 6, 8]
print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]

# Output: [1, 3, 5, 7]
print(odd)



#We can add one item to a list using append() method or add several items using extend() method.


odd = [1, 3, 5]

odd.append(7)

# Output: [1, 3, 5, 7]
print(odd)

odd.extend([9, 11, 13])

# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)




#We can also use + operator to combine two lists. This is also called concatenation.

#The * operator repeats a list for the given number of times.



odd = [1, 3, 5]

# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])

#Output: ["re", "re", "re"]
print(["re"] * 3)




#Furthermore, we can insert one item at a
# desired location by using the method insert() or insert multiple items by squeezing it into an empty slice of a list.



odd = [1, 9]
odd.insert(1,3)

# Output: [1, 3, 9]
print(odd)

odd[2:2] = [5, 7]

# Output: [1, 3, 5, 7, 9]
print(odd)