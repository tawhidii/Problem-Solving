
class Solution:

    def maxProductDifference(self, nums):
        nums.sort()
        min_prod = nums[0] * nums[1]
        max_prod = nums[-2] * nums[-1]
        return max_prod - min_prod


s = Solution()
print(s.maxProductDifference([5,6,2,7,4]))