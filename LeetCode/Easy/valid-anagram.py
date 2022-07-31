class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s,count_t = dict(),dict()
        for value in s:
            if value in count_s:
                count_s[value] +=1
            else:
                count_s[value] = 1
        for value in t:
            if value in count_t:
                count_t[value] +=1
            else:
                count_t[value] = 1
        
        for key in count_s.keys():
            if count_t.get(key,0) != count_s[key]:
                return False
        return True
        

s = Solution()
print(s.isAnagram('anagram','nagaram'))