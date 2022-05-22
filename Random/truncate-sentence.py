class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        result = []
        s_arr = s.split()
        for i in range(k):
            result.append(s_arr[i])
        return " ".join(result)


s = Solution()
print(s.truncateSentence("chopper is not a tanuki",5))