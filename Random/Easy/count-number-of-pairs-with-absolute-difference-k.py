
from itertools import combinations

class Solution:
    def countKDifference(self, nums, k):
        res = 0
        comb = list(combinations(nums,2))
        for value in comb:
            if abs(value[0]-value[1]) == k:
                res += 1
        return res
        
        # result = 0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] - nums[j] == k:
        #             result+=1
        # return result




s = Solution()
s.countKDifference([1,2,2,1],1)