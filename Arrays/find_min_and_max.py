

def getMinMax(a, n):
    max_value = a[0]
    min_value = a[0]
    for i in range(len(a)):
        if a[i] > max_value:
            max_value = a[i]
    for j in range(len(a)):
        if a[j] < min_value:
            min_value = a[j]
    return [min_value, max_value]


print(getMinMax([4, 1, 8, 9, 13, 12, 14, 7], 6))
