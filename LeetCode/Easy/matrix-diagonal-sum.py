class Solution:
    def diagonalSum(self, mat):
        n = len(mat)
        d_one = 0
        d_two = 0
        for i in range(n):
            d_one += mat[i][i]
            d_two += mat[i][n-i-1]
        if n%2 != 0:
            return d_one+d_two - mat[n//2][n//2]
        return d_one + d_two

s = Solution()
print(s.diagonalSum([[1,2,3],
              [4,5,6],
              [7,8,9]]))


