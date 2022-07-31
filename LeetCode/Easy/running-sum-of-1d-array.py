class Solution:
    def runningSum(self, nums):
        sum_  = 0 
        for i in range(len(nums)):
            sum_ = sum_ + nums[i]
            nums[i] = sum_
        return nums
        
