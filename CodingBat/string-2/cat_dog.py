def cat_dog(str):
    cat = 'cat'
    dog = 'dog'
    count_cat = 0
    count_dog = 0
    for i in range(len(str)):
        check = str[i:len(dog)+i]
        if check == cat:
            count_cat += 1
        if check == dog:
            count_dog += 1
    if count_cat == count_dog:
        return True
    return False


ans = cat_dog('catcat')
print(ans)
