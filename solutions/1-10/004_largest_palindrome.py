from solutions.common.is_palindrome import is_palindrome

min = 100
pal = 0
max = 1000
for i in range(min, max):
    j = i
    while j < max:
        prod = i * j
        pal = prod if (is_palindrome(prod) and prod > pal) else pal
        j += 1
print('max palindrome is {0}'.format(pal))
