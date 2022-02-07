# User function Template for python3
class Solution:
    # Just print the space seperated array elements
    def printArray(self, arr, n):
        # code here
        result = ""
        for i in range(n):
            result += str(arr[i]) + " "
        print(result)


s = Solution()
print(s.printArray([2, 3, 5, 5], 4))
