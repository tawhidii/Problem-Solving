class Solution:

    def print2largest(self, arr, n):
        value = list(set(arr))
        if len(value) > 1:
            value.sort()
            return value[-2]
        else:
            return -1


s = Solution()
print(s.print2largest([5, 10, 10], 6))
