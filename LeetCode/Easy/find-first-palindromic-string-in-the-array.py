

class Solution:
    def firstPalindrome(self, words):
        result = []
        for word in words:
            if word == word[::-1]:
                return word
        return ""
    


s = Solution()
print(s.firstPalindrome(["abc","car","cool"]))