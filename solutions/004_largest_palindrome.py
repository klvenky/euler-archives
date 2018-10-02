#!/usr/bin/python3
import sys
sys.path.append('../common/')
from common import is_palindrome as is_pal
min = 100
pal = 0
max = 1000
for i in range(min, max):
    j = i
    while j < max:
        prod = i * j
        pal = prod if (is_pal.is_palindrome(prod) and prod > pal) else pal
        j += 1
print('max palindrome is {0}'.format(pal))
