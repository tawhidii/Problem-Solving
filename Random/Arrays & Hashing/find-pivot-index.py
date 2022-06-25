class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0
        for index,_ in enumerate(nums):
            total -= nums[index]
            if total == left_sum:
                return index
            else:
                left_sum  += nums[index]
        return -1


s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))