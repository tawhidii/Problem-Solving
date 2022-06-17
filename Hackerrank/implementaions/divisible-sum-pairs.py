def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for i in range(n):
        for j in range(1,n):
            if i<j:
                sum_ = ar[i] + ar[j]
                if sum_ % k == 0:
                    count +=1
    return count



ans = divisibleSumPairs(6,3,[1, 3, 2, 6, 1, 2])
print(ans)
