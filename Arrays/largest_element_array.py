def largest(arr, n):
    i = 0
    max_value = arr[0]
    while i < n:
        if arr[i] > max_value:
            max_value = arr[i]
        i = i+1
    return max_value


largest([1, 8, 7, 56, 90], 5)
