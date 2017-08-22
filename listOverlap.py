#!/usr/bin/python3
#listOverlap.py: compares 2 lists and returns a list that contains only elements that appear in both lists.

import random

a = []

b = []

c = []

for i in range(random.randint(1,100)):
    a.append(random.randrange(1,1001,1))

for i in range(random.randint(1,100)):
    b.append(random.randrange(1,1001,1))

for elem in a:
    if elem in b:
        if elem not in c:
            c.append(elem)
        
for elem in b:
    if elem in a:
        if elem not in c:
            c.append(elem)

#d = list(set(c))

print("a = ")
a.sort()
print(a)
print("b = ")
b.sort()
print(b)
print("c = ")
c.sort()
print(c)
