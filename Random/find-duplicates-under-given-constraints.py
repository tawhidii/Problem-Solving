
def findDuplicate(A):
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            return A[i]

print(findDuplicate([1, 2, 3, 3, 3, 3, 3, 5, 9, 10]))