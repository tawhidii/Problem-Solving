class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        middle = (start+end)//2
        while nums[middle] != target and start<=end:
            if target>nums[middle]:
                start = middle + 1
            else:
                end = middle - 1
            middle = (start+end)//2
            print(start,middle,end)
        if(nums[middle] == target):
            return middle
        return -1
        
s = Solution()
print(s.search([-1,0,3,5,9,12],19))