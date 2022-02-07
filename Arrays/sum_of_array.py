# User function Template for python3
class Solution:

    def _sum(self, arr, n):
        i = 0
        summ = 0
        while i < n:
            summ += arr[i]
            i += 1
        return summ


s = Solution()
s._sum([1, 2, 3, 4], 4)
