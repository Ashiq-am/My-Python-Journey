quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.rfind('things', 10))

# Substring is searched in ' small things with great love'
print(quote.rfind('t', 2))

# Substring is searched in 'hings with great lov'
print(quote.rfind('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.rfind('th', 6, 20))