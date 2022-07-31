class Solution:
    def getConcatenation(self,nums):
        ans = []
        for v in nums:
            ans.append(v)
        return nums + ans


s = Solution()
print(s.getConcatenation([1,2,1]))