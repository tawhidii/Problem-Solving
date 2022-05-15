class Solution: 
    def select(self, arr, i):
        pass

    
    def selectionSort(self, arr,n):
        min = 0
        temp = 0
        for i in range(n-1):
            min = i 
            for j in range(i+1,n):
                if arr[j] < arr[min]:
                    min = j
            if min != i:
                temp = arr[i]
                arr[i] = arr[min]
                arr[min] = temp

        return arr


s = Solution()
print(s.selectionSort([4, 1, 3, 9, 7],5))
