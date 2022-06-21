def countingValleys(steps, path):
    level = 0
    valley = 0
    for p in path:
        if p == 'U':
            level+=1
        elif p== 'D':
            level -=1
        if level == 0 and p == 'U':
            valley +=1
    return valley


print(countingValleys(8,'UDDDUDUU'))