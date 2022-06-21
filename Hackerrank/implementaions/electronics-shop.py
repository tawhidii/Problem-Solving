def getMoneySpent(keyboards, drives, b):
    combinations = []
    
    for keybord in keyboards:
        for drive in drives:
            if keybord + drive <= b:
                combinations.append(sum([keybord,drive]))

    
    return -1 if len(combinations) == 0 else max(combinations)

print(getMoneySpent([40,50,60],[5,8,12],60))