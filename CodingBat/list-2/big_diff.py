def big_diff(nums):
    max_value = nums[0]
    min_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    return max_value - min_value


ans = big_diff([2, 10, 7, 2])
print(ans)
