def divisible_by_all_in_list(targetNum, numList):
    for num in numList:
        if targetNum % num:
            return False
    return True


def lcm(listNums):
    listNums.sort()
    out = 0
    min = max(listNums)
    while True:
        is_div = divisible_by_all_in_list(min, listNums)
        if is_div:
            out = min
            break
        min += 1
    return out
