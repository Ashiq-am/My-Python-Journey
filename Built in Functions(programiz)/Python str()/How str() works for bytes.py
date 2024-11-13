#If encoding and errors parameter is provided, the first parameter, object,
# should be a bytes-like-object (bytes or bytearray).

#If the object is bytes or bytearray, str() internally calls bytes.decode(encoding, errors).

#Otherwise, it gets the bytes object in the buffer before calling the decode() method.







# bytes
b = bytes('pythön', encoding='utf-8')
print(str(b, encoding='ascii', errors='ignore'))










#Here, the character 'ö' cannot be decoded by ASCII. Hence, it should give an error.
# However, we have set the errors ='ignore'. Hence, Python ignores the character which cannot be decoded by str().




