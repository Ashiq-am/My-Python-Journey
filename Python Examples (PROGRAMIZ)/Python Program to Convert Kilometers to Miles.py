# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))








'''Here, the user is asked to enter kilometers. This value is stored in the kilometers variable.


Since 1 kilometer is equal to 0.621371 miles, we can get the equivalent miles by multiplying kilometers with this factor.



Your turn: Modify the above program to convert miles to kilometers using the following formula and run it.

kilometers = miles / conv_fac'''