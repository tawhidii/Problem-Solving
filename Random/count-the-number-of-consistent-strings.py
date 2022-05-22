
class Solution:
    def countConsistentStrings(self, allowed, words):
        result = 0
        allowed_set = set(allowed)
        for word in words:
            if not set(word).difference(allowed_set):
                result +=1
        
        return result

s = Solution()
s.countConsistentStrings('abc',["a","b","c","ab","ac","bc","abc"])