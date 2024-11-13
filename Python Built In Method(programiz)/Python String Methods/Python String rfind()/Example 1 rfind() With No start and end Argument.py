quote = 'Let it be, let it be, let it be'

result = quote.rfind('let it')
print("Substring 'let it':", result)

result = quote.rfind('small')
print("Substring 'small ':", result)

result = quote.rfind('be,')
if  (result != -1):
  print("Highest index where 'be,' occurs:", result)
else:
  print("Doesn't contain substring")