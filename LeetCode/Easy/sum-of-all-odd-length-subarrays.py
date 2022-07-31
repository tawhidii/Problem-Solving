

class Solution:
    def sumOddLengthSubarrays(self, arr):
        n = len(arr) + 1
        result = 0
        for i in range(n):
            if i % 2 == 1:
                for j in range(n-i):
                    result += sum(arr[j:i+j])
        return result

s = Solution()
print(s.sumOddLengthSubarrays([1,4,2,5,3]))