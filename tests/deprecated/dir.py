import os
from os.path import expanduser

home = expanduser("~\Desktop")
h = os.listdir(home)
str1 = '\n'.join(h)


print(str1)
