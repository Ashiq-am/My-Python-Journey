text = "programming is easy"
result = text.startswith(('python', 'programming'))

# prints True
print(result)

result = text.startswith(('is', 'easy', 'java'))

# prints False
print(result)

# With start and end parameter
# 'is easy' string is checked
result = text.startswith(('programming', 'easy'), 12, 19)

# prints False
print(result)