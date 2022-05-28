class Solution:
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:
        result = 0
        length = len(arr)
        for i in range(length-2):
            for j in range(i+1,length-1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1,length):
                        if abs(arr[j]-arr[k])<=b and abs(arr[i] - arr[k]) <=c:
                            result +=1
        return result



s = Solution()
print(s.countGoodTriplets([3,0,1,1,9,7],7,2,3))
