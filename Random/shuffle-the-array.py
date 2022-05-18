
from cgitb import reset


class Solution:
    def shuffle(self, nums, n):
        result = []
        y_items = nums[n:2*n]
        for i in range(n):
            result.append(nums[i])
            result.append(y_items[i])
        return result

s = Solution()
print(s.shuffle([2,5,1,3,4,7],3))