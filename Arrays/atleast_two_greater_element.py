# User function Template for python3


class Solution:
    def findElements(self, a, n):
        sorted_arr = sorted(a)
        result = []
        for i in range(len(sorted_arr)-2):
            result.append(sorted_arr[i])

        return result


s = Solution()
s.findElements([2, 8, 7, 1, 5], 5)
