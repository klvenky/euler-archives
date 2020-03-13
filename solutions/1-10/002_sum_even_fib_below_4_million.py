a = 0
b = 1
sum = 0
while b<4000000:
    b = a+ b
    a = b-a
    if not b % 2 :
        sum += b
print('sum of even fibanocii numbers below 4 million is {0}'.format(sum))