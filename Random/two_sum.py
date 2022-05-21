class Solution:
 
    def twoSum(self, nums, target):
        seen = {}
        for idx in range(len(nums)):
            remaining = target - nums[idx]
            if remaining in seen:
                return [seen[remaining], idx]
            seen[nums[idx]] = idx


sol = Solution()
ans = sol.twoSum([2, 7, 11, 15, 22, 8, 19], 9)
print(ans)
