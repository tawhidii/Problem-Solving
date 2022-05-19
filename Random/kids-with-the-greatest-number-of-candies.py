
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxCandyValue = max(candies)
        return [maxCandyValue <= candy + extraCandies for candy in candies]
        # result = []
        # for i in range(len(candies)):
        #     value = candies[i] + extraCandies
        #     if value>= max(candies):
        #         result.append(True)
        #     else:
        #         result.append(False)
        # return result
s = Solution()
print(s.kidsWithCandies([12,1,12],10))