class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        arr = [0]
        for g in gain:
            arr.append(arr[-1]+g)
        max_ = 0
        for i in arr:
            if i>max_:
                max_ = i
        return max_
        
        

s = Solution()
print(s.largestAltitude([-5,1,5,0,-7]))