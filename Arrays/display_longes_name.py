class Solution:
    def longest(self, names, n):
        # code here
        first_name_len = len(names[0])
        for name in names:
            if len(name) > first_name_len:
                first_name_len = len(name)
        result = ""
        for name in names:
            if len(name) == first_name_len:
                result = name
        return result


solution = Solution()
solution.longest(["Geek", "Geeks", "Geeksfor",
                  "GeeksforGeek", "GeeksforGeeks"], 5)
