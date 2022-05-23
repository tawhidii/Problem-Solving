
class Solution:
    def countPairs(self, nums, k: int):
        result = 0
        length = len(nums)
        for i in range(length):
            for j in range(i+1,length):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    result += 1
        return result
                    



s = Solution()

print(s.countPairs([5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3],7))