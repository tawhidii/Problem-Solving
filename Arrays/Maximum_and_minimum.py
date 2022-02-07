def solution():
    t = int(input())
    for i in range(t):
        size = int(input())
        arr = list(map(int, input().split()))

        min_value = arr[0]
        max_value = arr[0]
        for i in arr:
            if i > max_value:
                max_value = i
                print(max_value)
            if i < min_value:
                min_value = i
                print(min_value)
        # print(max_value, min_value)


solution()
