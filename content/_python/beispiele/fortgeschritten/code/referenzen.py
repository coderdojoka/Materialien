__author__ = 'Mark Weinreuter'

from pyenguin import *

fenster = Fenster()
print(fenster)
print(hex(id(fenster)))

l1 = [1, 2, 3]
l2 = l1
l2.append(4)
l3 = [1, 2, 3, 4]

print("l1: ", id(l1))
print("l2: ", id(l2))
print("l3: ", id(l3))


x = 5
y = 5
print(id(x), id(y))
x = 6
print(id(x), id(y))
