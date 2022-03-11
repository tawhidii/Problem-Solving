def first_two(str):
    if len(str) <= 2:
        return str
    return str[:2]


ans = first_two('abcdefg')
print(ans)
