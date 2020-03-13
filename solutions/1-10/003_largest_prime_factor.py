#!/usr/bin/python3
from solutions.common.is_prime import is_prime
max = 600851475143
num = max // 2 + 1
num = num if num % 2 else num + 1
out = None
print(max)
print(num)
while num > 1:
    if not max % num:
        print('divisor -- ', num)
        if is_prime(num):
            print('found {0}', num)
            out = num
            break
    num -= 2
out = 2 if not out and not max % 2 else out
out = max if not out else out

print('larget prime factor is {0}'.format(out))
