# User function Template for python3
from os import name


class Solution:

    def swapKth(self, arr, n, k):
        # code here
        positive_k = arr[k-1]
        negative_k = arr[-k]
        arr[k-1] = negative_k
        arr[-k] = positive_k
        return arr


sol = Solution()
ans = sol.swapKth([1, 2, 3, 4, 5, 6, 7, 8], 8, 3)
print(ans)
