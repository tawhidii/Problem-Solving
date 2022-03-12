def same_first_last(nums):
    return len(nums)>= 1 and nums[len(nums)-1] == nums[0]


ans = same_first_last([1, 2, 1])
print(ans)
