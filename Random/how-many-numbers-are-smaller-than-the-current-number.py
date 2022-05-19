
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        count = 0
        result = []
        for i in range(len(nums)):
            for  j in range(len(nums)):
                if nums[i]>nums[j]:
                    count +=1
            result.append(count)
            count = 0
        return result



s = Solution()

print(s.smallerNumbersThanCurrent([7,7,7,7]))
