def front_back(str):
    if len(str) <= 1:
        return str
    front = str[0]
    back = str[len(str)-1]
    middle = str[1:len(str)-1]
    return back + middle + front


print(front_back('ab'))
