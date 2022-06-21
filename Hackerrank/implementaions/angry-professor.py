def angryProfessor(k, a):
    on_time = 0
    for value in a:
        if value<=0:
            on_time += 1
    if k <= on_time: 
        return "NO"
    else:
        return "YES"
    

print(angryProfessor(10,[-93,-86,49,-62,-90,-63,40,72,11,67]))
