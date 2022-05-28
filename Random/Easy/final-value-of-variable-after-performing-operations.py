
class Solution:
    def finalValueAfterOperations(self, operations):
        result = 0
        for operation in operations:
            if '+' in operation:
                result += 1
            if '-' in operation:
                result -=1
        return result
        # result = 0
        # i = 0
        # while(i<len(operations)):
        #     print(operations[i])
        #     if operations[i] == '--X':
        #         result = result - 1
        #     if operations[i] == 'X++':
        #         result = result + 1
        #     if operations[i] == '++X':
        #         result = result + 1
        #     if operations[i] == 'X--':
        #         result = result - 1 
        #     i+=1
        # return result

s = Solution()
ans = s.finalValueAfterOperations(["X++","++X","--X","X--"])
print(ans)