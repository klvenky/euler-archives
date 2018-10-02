start = 3
sum = 0
for num in range(1000):
    if not num % 3 or not num % 5:
        sum += num
print('sum is {0}', sum)
