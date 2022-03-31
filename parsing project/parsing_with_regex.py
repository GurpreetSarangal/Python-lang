import re

my_string = "Names : Romeo, Juliet"
names = [name.strip() for name in my_string.split(':')[1].split(',')]
print(names)