class Solution:
    def decompressRLElist(self, nums):
        i = 0
        result = []
        while(i<len(nums)):
            result += [nums[i+1]] * nums[i] 
            i+=2
        return result
 

s = Solution()
s.decompressRLElist([1,2,3,4])
