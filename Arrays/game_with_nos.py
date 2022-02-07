def game_with_number(arr,  n):
    for i in range(len(arr)-1):
        arr[i] = arr[i] ^ arr[i+1]
    return arr


game_with_number([10, 11, 1, 2, 3], 5)
