nums = list(map(int, input().split()))
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

str_list = [str(num) for num in nums]
print(" ".join(str_list))
