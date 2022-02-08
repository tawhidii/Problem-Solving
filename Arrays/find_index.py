class Solution:
    def findIndex(self, a, N, key):

        start = -1

        for i in range(N):
            if(a[i] == key):
                start = i
                break

        end = start

        for j in range(N-1, start-1, -1):

            if(a[j] == key):
                end = j
                break

        if (start == end):
            return start, start

        else:
            return start, end


s = Solution()
