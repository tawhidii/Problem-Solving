# def array_front9(nums):
#     if len(nums) < 4:
#         if 9 in nums:
#             return True
#     lst = []
#     for i in range(len(nums)-1):
#         lst.append(nums[i])
#     if 9 in lst:
#         return True
#     return False


# ans = array_front9([1, 2, 3, 4, 5])
# print(ans)

# alternate solution
def array_front9(nums):
    end = len(nums)
    if end > 4:
        end = 4
    for i in range(end):
        if nums[i] == 9:
            return True
    return False
