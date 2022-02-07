def solution():
    t = int(input())
    for i in range(t):
        size = int(input())
        arr_input = list(map(int, input().split()))
        print(*arr_input[::-1])


# ans = solution()
# print(ans)

listtt = [1, 3, 4, 5, 6, 6]
print(*listtt)
