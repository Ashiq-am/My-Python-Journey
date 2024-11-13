#We can delete one or more items from a list using the keyword del. It can even delete the list entirely.


my_list = ['p','r','o','b','l','e','m']

# delete one item
del my_list[2]

# Output: ['p', 'r', 'b', 'l', 'e', 'm']
print(my_list)

# delete multiple items
del my_list[1:5]

# Output: ['p', 'm']
print(my_list)

# delete entire list
del my_list

# Error: List not defined
print(my_list)





# We can use remove() method to remove the given item or pop() method to remove an item at the given index.

# The pop() method removes and returns the last item if index is not provided.
# This helps us implement lists as stacks (first in, last out data structure).

# We can also use the clear() method to empty a list.



my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)




#Finally, we can also delete items in a list by assigning an empty list to a slice of elements.

my_list = ['p','r','o','b','l','e','m']
my_list[2:3] = []
my_list = ['p', 'r', 'b', 'l', 'e', 'm']
my_list[2:5] = []
my_list = ['p', 'r', 'm']