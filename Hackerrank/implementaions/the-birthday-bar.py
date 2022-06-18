def birthday(s, d, m):
    # Write your code here
    count = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            count +=1
    return count

birthday([1,2,1,3,2],3,2)