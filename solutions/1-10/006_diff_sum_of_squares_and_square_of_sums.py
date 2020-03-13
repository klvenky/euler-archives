#!/usr/bin/python3
max = 101
sum = 0
square_sum = 0
for num in range(max):
    sum += num
    square_sum += num ** 2
print(sum)
print(square_sum)
print('difference is -->> ',sum ** 2 - square_sum)
