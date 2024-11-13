s = {0: 'False', 1: 'False'}
print(all(s))

s = {1: 'True', 2: 'True'}
print(all(s))

s = {1: 'True', False: 0}
print(all(s))

s = {}
print(all(s))

# 0 is False
# '0' is True
s = {'0': 'True'}
print(all(s))