#User function Template for python3

from re import A


class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        for i in range(n-1):
            for j in range(n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr


s = Solution()
print(s.bubbleSort([4, 1, 3, 9, 7],5))
        
