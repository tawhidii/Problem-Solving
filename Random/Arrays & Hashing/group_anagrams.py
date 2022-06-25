class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_ = {}
        for str in strs:
            sorted_str = "".join(sorted(list(str)))
            if sorted_str not in dict_:
                dict_[sorted_str] = [str]
            else:
                dict_[sorted_str].append(str)
        return list(dict_.values())


s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))