def is_prime(num):
    out = True
    if num < 2 :
        out = False
    elif num == 2:
        out = True
    else:
        half = num // 2 + 1
        for tmp in range(2, half):
            if not num % tmp:
                out = False
                break
    return out
# print(is_prime(101))
