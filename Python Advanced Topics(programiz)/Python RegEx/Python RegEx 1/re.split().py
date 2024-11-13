
import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string)
print(result)

# Output: ['Twelve:', ' Eighty nine:', '.']



#If the pattern is no found, re.split() returns a list containing an empty string.

#You can pass maxsplit argument to the re.split() method. It's the maximum number of splits that will occur.




import re

string = 'Twelve:12 Eighty nine:89 Nine:9.'
pattern = '\d+'

# maxsplit = 1
# split only at the first occurrence
result = re.split(pattern, string, 1)
print(result)

# Output: ['Twelve:', ' Eighty nine:89 Nine:9.']


#By the way, the default value of maxsplit is 0; meaning all possible splits.