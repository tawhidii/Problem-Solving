# class Solution:
#     def countMatches(self, items, ruleKey, ruleValue):
#         count = 0
#         storage = []
#         for v in items:
#             data = {}
#             type,color,name = v 
#             data['type'] = type
#             data['color'] = color
#             data['name'] = name
#             storage.append(data)

#         for item in storage:
#             if item[ruleKey]==ruleValue:
#                 count+=1
#         return count
        
# s = Solution()
# print(s.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],"type","phone"))


# clean solution 
class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        count = 0
        keys = {'type':0,'color':1,'name':2}
        for item in items:
            if item[keys[ruleKey]] == ruleValue:
                count +=1
        return count

        
s = Solution()
print(s.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],"type","phone"))
