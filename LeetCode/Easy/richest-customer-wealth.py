# class Solution:
#     def getTotalWealth(self,account):
#         total = 0
#         for value in account:
#             total += value
#         return total

#     def maximumWealth(self, accounts):
#         result = 0
#         for acc in accounts:
#             get_total = self.getTotalWealth(acc)
#             if get_total > result:
#                 result = get_total
#         return result


class Solution:
    def maximumWealth(self, accounts):
        result = 0
        for acc in accounts:
            sm = sum(acc)
            if sm>result:
                result = sm
            
        return result


s = Solution()
print(s.maximumWealth([[1,5],[7,3],[3,5]]))