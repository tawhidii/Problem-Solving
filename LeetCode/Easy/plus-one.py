class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = "".join([str(i) for i in digits])
        cal = str(int(digits)+1)
        return [int(i) for i in cal]


s = Solution()
print(s.plusOne([1,2,3]))