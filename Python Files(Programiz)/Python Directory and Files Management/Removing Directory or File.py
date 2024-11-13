os.listdir()
['new_one', 'old.txt']

os.remove('old.txt')
os.listdir()
['new_one']


os.rmdir('new_one')
os.listdir()
[]










os.listdir()
['test']

os.rmdir('test')
Traceback (most recent call last):
...
OSError: [WinError 145] The directory is not empty: 'test'

import shutil

shutil.rmtree('test')
os.listdir()
[]