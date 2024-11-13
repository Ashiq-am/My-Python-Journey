# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)






#In this program, we loop until the user enters an integer that has a valid reciprocal.
# The portion that can cause exception is placed inside try block.
# If no exception occurs, except block is skipped and normal flow continues.
# But if any exception occurs, it is caught by the except block.Here,
# we print the name of the exception using ex_info() function inside sys module and ask the user to try again.
# We can see that the values 'a' and '1.3' causes ValueError and '0' causes ZeroDivisionError.