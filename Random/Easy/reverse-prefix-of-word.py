

class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        word_list = list(word)
        left = 0
        right = 0
        for i in range(len(word_list)):
            if word_list[i] == ch:
                right = i
                break
        while(left<=right):
            word_list[left],word_list[right] = word_list[right],word_list[left]
            left+=1
            right -=1
        return "".join(word_list)

s = Solution()
print(s.reversePrefix('xyxzxe','z'))