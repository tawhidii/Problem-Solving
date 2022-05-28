
class Solution:
    def prefixCount(self, words, pref):
        count = 0
        for word in words:
            if word.startswith(pref):
                count +=1
        return count


s = Solution()
ans= s.prefixCount(["pay","attention","practice","attend"],'at')
print(ans)
