class Solution:
    def countGoodRectangles(self, rectangles):
        minLen = [min(rectangle) for rectangle in rectangles]
        maxLen = max(minLen)
        return minLen.count(maxLen)



s = Solution()
s.countGoodRectangles([[5,8],[3,9],[5,12],[16,5]])