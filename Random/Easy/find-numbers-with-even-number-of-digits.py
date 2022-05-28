class Solution:
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            len_  = len(str(num))
            if len_ % 2 == 0:
                count +=1
        return count