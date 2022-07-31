class Solution:
    def divideArray(self, nums):
        not_pair = set()
        for num in nums:
            if num not in not_pair:
                not_pair.add(num)
            else:
                not_pair.remove(num)
        
        return not not_pair


s = Solution()
print(s.divideArray([1,2,3,4]))