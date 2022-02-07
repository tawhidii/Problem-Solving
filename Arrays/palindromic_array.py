# Your task is to complete this function
# Function should return True/False or 1/0


def PalinArray(arr, n):
    return all(str(i) == str(i)[::-1] for i in arr)


ans = PalinArray([111, 222, 333, 444, 555], 5)
print(ans)
