def first_half(str):
    half = int(len(str) / 2)
    print(half)
    return str[:half]


ans = first_half('HelloThere')
print(ans)
