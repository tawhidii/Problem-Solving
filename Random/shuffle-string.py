class Solution:
    def restoreString(self, s, indices):
        res = ''
        storage = {}
        for idx,st in zip(indices,s):
            storage[idx] = st
        for i in sorted(storage.items()):
            res += i[1]
        return res
        # storage = {}
        # res = ''
        # for i in range(len(s)):
        #     storage[indices[i]] = s[i]
        
        # for key in sorted(storage.keys()):
        #     res += storage[key]
        # return res



s = Solution()
print(s.restoreString('codeleet',[4,5,6,7,0,2,1,3]))
