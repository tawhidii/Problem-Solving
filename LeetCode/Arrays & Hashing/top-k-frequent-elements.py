class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_frequency = {}
        result = []
        for num in nums:
            if num in nums_frequency:
                nums_frequency[num] +=1
            else:
                nums_frequency[num] = 1
        
        result = sorted(nums_frequency,key=nums_frequency.get,reverse=True)

        return result[:k]
        


s = Solution()
print(s.topKFrequent([1,1,1,2,2,3],2))