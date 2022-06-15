class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s_list = list(s)
        left = 0
        right = len(s_list) - 1
        while(left<=right):
            if s_list[left] in vowels and s_list[right] in vowels:
                s_list[left],s_list[right] = s_list[right],s_list[left]
                left+= 1
                right-= 1
            else:
                if s_list[left] not in vowels:
                    left += 1
                if s_list[right] not in vowels:
                    right -= 1
        return "".join(s_list)

s = Solution()
print(s.reverseVowels("A man, a plan, a canal: Panama"))