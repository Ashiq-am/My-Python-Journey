# Program to count the number of each vowels

# string of vowels
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)





"""Here, we have taken a string stored in ip_str. 
Using the method casefold(), we make it suitable for caseless comparisons. 
Basically, this method returns a lowercased version of the string.

We use the dictionary method fromkeys() to construct a new dictionary with each vowel as its key and all values equal to 0. 
This is the initialization of the count."""