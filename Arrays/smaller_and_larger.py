# User function Template for python3
class Solution:

    def getMoreAndLess(self, arr, n, x):
        smaller_ = 0
        larger_ = 0
        for i in range(n):
            if arr[i] >= x:
                larger_ += 1
            if arr[i] <= x:
                smaller_ += 1
        return smaller_, larger_


s = Solution()
s.getMoreAndLess([1, 2, 8, 10, 11, 12, 19], 7, 0)
