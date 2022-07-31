
# time comeplexy = o(n)
class Solution(object):

        
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum_value = max(nums)
        idx = nums.index(maximum_value)
        nums.remove(maximum_value)
        count = 0
        for val in nums:
            if maximum_value>=val*2:
                count +=1 
        if count == len(nums):
            return idx
        return -1       

s = Solution()
print(s.dominantIndex([3,6,1,0]))