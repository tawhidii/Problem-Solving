






def migratoryBirds(arr):
    count = [arr.count(i) for i in range(1,6)]
    print(count)
    for i in range(len(count)):
        if count[i] == max(count):
            return i + 1


    # arr.sort()
    # bird_freq = {}
    # for val in arr:
    #     if val in bird_freq:
    #         bird_freq[val] +=1
    #     else:
    #         bird_freq[val] = 1
    # max_value = 0
    # for key in bird_freq.keys():
    #     if bird_freq[key] > max_value:
    #         max_value = bird_freq[key]
    # for key,value in bird_freq.items():
    #     if value == max_value:
    #         return key


import os
cwd = os.getcwd()
file = open('/home/system32/Desktop/CODE/Solving/Hackerrank/implementaions/test.txt','r')
data = file.read()
data_to_str = data.replace(' ','')
lst = [ int(i) for i in data_to_str]


ans = migratoryBirds([1,4,4,4,5,3])
print(ans)