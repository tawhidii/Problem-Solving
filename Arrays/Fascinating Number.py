# User function Template for python3
from re import T


class Solution:

    def fascinating(self, n):
        mul_two = str(2*n)
        mul_three = str(3*n)
        to_list = list(str(n)+mul_two+mul_three)
        to_int = list(map(int, to_list))
        to_int.sort()
        if to_int == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return True
        else:
            return False


s = Solution()
print(s.fascinating(853))
