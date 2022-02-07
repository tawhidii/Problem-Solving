# User function Template for python3
class Solution:

    def valueEqualToIndex(self, arr, n):
        i = 0
        result = []
        while i < n:
            if arr[i] == i+1:
                result.append(arr[i])
            i += 1

        return result


s = Solution()
print(s.valueEqualToIndex([15, 2, 45, 12, 7], 5))
