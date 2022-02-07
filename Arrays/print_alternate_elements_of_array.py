
# User function Template for python3

# arr is the array
# n is the number of elements in array
def printAl(arr, n):
    result = []
    for i in range(len(arr)):
        if i % 2 == 0:
            print(arr[i], end=" ")


printAl([1, 2, 3, 4], 4)
