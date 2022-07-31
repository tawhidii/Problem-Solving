class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            start = 0
            end = len(row) - 1
            while(start<=end):
                mid = (start+end)//2
                if row[mid] == target:
                    return True
                if target>row[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False

    

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))