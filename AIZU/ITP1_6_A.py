n = int(input())
values = list(map(int, input().split()))
result = []
for val in reversed(values):
    result.append(val)

print(' '.join(map(str, result)))
