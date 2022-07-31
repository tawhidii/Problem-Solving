class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = 0
        for idx,val in enumerate(nums):
            if val % 2 == 0:
                temp = nums[pos]
                nums[pos] = nums[idx]
                nums[idx] = temp
                pos +=1
        return nums



s = Solution()
ans = s.sortArrayByParity([3,1,2,4])
print(ans)