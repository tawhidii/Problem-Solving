def pickingNumbers(a):
    # Write your code here
    max_ = 0
    for value in a:
        x = a.count(value)
        y = a.count(value-1)
        c = x+y
       

        if c > max_:
            max_ = c
    return max_



print(pickingNumbers([4,6,5,3,3,1]))