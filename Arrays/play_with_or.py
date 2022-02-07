def game_with_number(arr,  n):
    # Complete the function
    for i in range(n-1):
        arr[i] = arr[i] | arr[i+1]

    return arr


print(game_with_number([10, 11, 1, 2, 3], 5))
