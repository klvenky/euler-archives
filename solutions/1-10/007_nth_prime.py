#!/usr/bin/python3
from solutions.common import is_prime as check_prime
now = 0
prime_count = 0
n = 10001
prime = None
while prime_count < n+1:
    if(check_prime.is_prime(now)):
        prime_count += 1
        prime = now
        if(prime_count == n):
            break
    now += 1
print(n, 'th prime is ', now)
