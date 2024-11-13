# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

values = sales.values()
print('Original items:', values)

# delete an item from dictionary
del[sales['apple']]
print('Updated items:', values)





#The view object values doesn't itself return a list of sales item values but it returns a view of all values of the dictionary.

#If the list is updated at any time, the changes are reflected on to the view object itself, as shown in the above program.