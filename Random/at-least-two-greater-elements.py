class Solution:
    def findElements(self, a, n):
        a.sort()
        result = []
        for i in range(n-2):
            result.append(a[i])
        return result


s = Solution()
print(s.findElements([2, 8, 7, 1, 5], 5))
