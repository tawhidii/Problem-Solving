def xyz_there(str):
    strr = 'xyz'
    for i in range(len(str)):
        if str[i:len(strr)+i] == strr and str[i-1] != '.':
            return True
    return False


ans = xyz_there('abc.xyz')
print(ans)
