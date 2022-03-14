

def count_hi(str):
    count = 0
    sub_str = 'hi'
    for i in range(len(str)):
        if str[i:len(sub_str)+i] == sub_str:
            count += 1

    return count


ans = count_hi('ABChi hi')
print(ans)
