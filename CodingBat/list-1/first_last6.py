def first_last6(nums):
    return nums[0] == 6 or nums[len(nums)-1] == 6


ans = first_last6([1, 2, 6])
print(ans)
