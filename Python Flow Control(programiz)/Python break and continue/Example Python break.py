# Use of break statement inside loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")



'''In this program, we iterate through the "string" sequence. We check if the letter is "i", upon which we break from the loop. 
Hence, we see in our output that all the letters up till "i" gets printed. After that, the loop terminates.'''