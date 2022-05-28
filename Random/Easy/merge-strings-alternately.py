

class Solution:
    def mergeAlternately(self, word1, word2):
        a = 0
        b = 0
        result = ""
        len_w1 = len(word1)
        len_w2 = len(word2)
        while a<len_w1 and b < len_w2:
            result += word1[a]
            result += word2[b]
            a+=1
            b+=1
        while a < len_w1:
            result += word1[a]
            a+=1
        
        while b < len_w2:
            result += word2[b]
            b+=1

        return result


s = Solution()
print(s.mergeAlternately('ab','pqrs'))


