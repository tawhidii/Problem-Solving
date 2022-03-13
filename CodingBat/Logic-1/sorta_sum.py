def sorta_sum(a, b):
    sum_ = a + b
    if sum_ < 10:
        return sum_
    if 10 <= sum_ < 20:
        return 20
    return sum_


ans = sorta_sum(3, 4)
print(ans)
