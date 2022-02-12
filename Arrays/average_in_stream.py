# User function Template for python3

class Solution:
    def streamAvg(self, arr, n):
        result = []
        sum_ = 0
        for i in range(n):
            div = i+1
            sum_ += arr[i]
            result.append(float(sum_/div))
        return result


s = Solution()
s.streamAvg([10, 20, 30, 40, 50], 5)
