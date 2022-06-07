# class Solution(object):
#     def reverseOnlyLetters(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         s_list = list(s)
#         left,right = 0,len(s_list) - 1
#         while left < right:
#             if not s_list[left].isalpha():
#                 left +=1
#             elif not s_list[right].isalpha():
#                 right -=1
#             else:
#                 s_list[left],s_list[right] = s_list[right],s_list[left]
#                 left +=1
#                 right -=1
#         return "".join(s_list)

# s = Solution()
# s.reverseOnlyLetters('a-bC-dEf-ghIj')

