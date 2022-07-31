class Solution:
    def mostWordsFound(self, sentences):
        max_len = 0
        for sen in sentences:
            get_len = len(sen.split())
            if get_len>max_len:
                max_len = get_len
        return max_len


s = Solution()
print(s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
