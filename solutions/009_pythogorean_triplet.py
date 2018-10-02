#!/usr/bin/python3
import math
a = 1
c = 0
max = 1000
found = False
while a < max and not found:
    a_sq = a ** 2
    b = a
    while b < max and a+b < max:
        tmp = a_sq + b ** 2
        c = math.sqrt(tmp)
        is_int = c.is_integer()
        if is_int and a+b+int(c) == max:
            print('a: {0} b: {1} c: {2} sum: {3} int: {4}'.format(a, b, c, a+b+c, is_int))
            c = int(c)
            found = True
            break
        b += 1
    if found:
        break
    a += 1
print('found ->> ', found)
if found:
    print('product is {0}'.format(a * b * c))
