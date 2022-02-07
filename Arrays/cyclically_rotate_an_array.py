def rotate(arr, n):
    value = arr.pop(len(arr)-1)
    arr.insert(0, value)

    # print(arr)
    return arr


print(rotate([9, 8, 7, 6, 4, 2, 1, 3], 8))
