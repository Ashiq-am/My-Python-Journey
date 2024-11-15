f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode








#Unlike other languages, the character 'a' does not imply the number 97 until it is encoded using ASCII (or other equivalent encodings).

#Moreover, the default encoding is platform dependent. In windows, it is 'cp1252' but 'utf-8' in Linux.

#So, we must not also rely on the default encoding or else our code will behave differently in different platforms.

#Hence, when working with files in text mode, it is highly recommended to specify the encoding type.



f = open("test.txt",mode = 'r',encoding = 'utf-8')