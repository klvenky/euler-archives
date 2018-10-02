#!/usr/bin/python3
from .. import is_prime
max = 2000000
sum = 0
for tmp in range(max):
    if(is_prime(tmp)):
        sum += tmp
