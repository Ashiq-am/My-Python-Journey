# Python rogram to find the SHA-1 message digest of a file

# importing the hashlib module
import hashlib

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

message = hash_file("track1.mp3")
print(message)




"""In this program, we open the file in binary mode. Hash functions are available in the hashlib module. 
We loop till the end of the file using a while loop. On reaching the end, we get empty bytes object.

In each iteration, we only read 1024 bytes (this value can be changed according to our wish) 
from the file and update the hashing function.

Finally, we return the digest message in hexadecimal representation using the hexdigest() method."""









'''Hash functions take an arbitrary amount of data and return a fixed-length bit string. 
The output of the function is called the digest message.

They are widely used in cryptography for authentication purposes. 
There are many hashing functions like MD5, SHA-1 etc. Refer this page to know more about hash functions in cryptography.

In this example, we will illustrate how to hash a file. We will use the SHA-1 hashing algorithm. 
The digest of SHA-1 is 160 bits long.

We do not feed the data from the file all at once, because some files are very large to fit in memory all at once. 
Breaking the file into small chunks will make the process memory efficient.'''