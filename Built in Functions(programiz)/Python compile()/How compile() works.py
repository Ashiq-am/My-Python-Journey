codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')

exec(codeObejct)










#Here, the source is in normal string form. The filename is sumstring.
# And, the exec mode later allows the use of exec() method.

#The compile() method converts the string to Python code object. The code object is then executed using exec() method.