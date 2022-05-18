

class Solution:
    def numIdenticalPairs(self, nums):
        countItems = {}
        result = 0
        for item in nums:
            if item in countItems:
                countItems[item] +=1
            else:
                countItems[item] = 1
        for key in countItems.keys():
            value = countItems[key]
            result += value * (value - 1) // 2

        return result 
            



s = Solution()

print(s.numIdenticalPairs([1,2,3,1,1,3]))