def near_hundred(n):
    return 100 - n <= 10 or 200 - n <= 10


print(near_hundred(89))
