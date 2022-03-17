def sum13(nums):
    s = 0
    i = 0
    while i < len(nums):
        print(i)
        if nums[i] == 13:
            i += 1
        else:
            s += nums[i]

        i += 1

    return s


ans = sum13([13, 1, 2, 13, 2, 1, 13])
print(ans)
