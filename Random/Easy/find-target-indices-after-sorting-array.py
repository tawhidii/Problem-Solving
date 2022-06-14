# --> Binary Search 


class Solution:
    def targetIndices(self, nums,target):
        nums.sort()
        start = 0
        end = len(nums) -1
        result = []
        while(start<=end):
            mid = (start+end)//2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        for i in range(start,len(nums)):
            if nums[i] == target:
                result.append(i)
        return result
        
s = Solution()
print(s.targetIndices([1,2,5,2,3],2))
        