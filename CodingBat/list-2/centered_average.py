def centered_average(nums):
    sum_ = 0
    max_value = nums[0]
    min_value = nums[0]
    for num in nums:
        sum_ += num
    for num in nums:
        if max_value < num:
            max_value = num
        if min_value > num:
            min_value = num
    result = int((sum_ - max_value - min_value) / (len(nums) - 2))
    return result


ans = centered_average([1, 2, 3, 4, 100])
print(ans)
