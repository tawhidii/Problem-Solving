class Solution:
    def decode(self, encoded,first):
        result = [first]
        for i in encoded:
            result.append(i^result[-1])
        return result


s = Solution()
print(s.decode([1,2,3],1))
