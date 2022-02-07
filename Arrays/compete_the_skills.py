# User function Template for python3


class Solution:
    def scores(self, a, b, cc):
        # Update list cc of length 2 with cc[0] = ca and cc[1] = cb
        # Your code goes here
        count_one = 0
        count_two = 0
        for i in range(3):
            if a[i] > b[i]:
                count_one += 1
            elif a[i] < b[i]:
                count_two += 1
            else:
                continue

        result = [count_one, count_two]
        return list(result)


s = Solution()
ans = s.scores([4, 2, 7], [5, 6, 3], 0)
print(ans)
