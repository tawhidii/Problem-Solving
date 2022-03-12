def max_end3(nums):
    if nums[0] > nums[-1]:
        return [nums[0], nums[0], nums[0]]
    if nums[-1] > nums[0]:
        return [nums[-1], nums[-1], nums[-1]]
    if nums[-1] == nums[0]:
        return [nums[0], nums[0], nums[0]]


ans = max_end3([2, 11, 3])
print(ans)
