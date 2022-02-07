
def countOfElements(a, n, x):
    result = []
    for i in range(n):
        if a[i] <= x:
            result.append(a[i])
    return len(result)


print(countOfElements([1, 2, 4, 5, 8, 10], 6, 9))
