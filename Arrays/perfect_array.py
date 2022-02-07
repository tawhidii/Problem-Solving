# User function Template for python3

class Solution:
    def IsPerfect(self, arr, n):
        resverse_arr = arr[::-1]
        if resverse_arr == arr:
            return True

        return False


s = Solution()
s.IsPerfect([1, 2, 3, 2, 5], 5)
