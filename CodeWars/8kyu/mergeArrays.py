



def merge_arrays(arr1, arr2):
    arr1.sort()
    arr2.sort()
    concat = arr1 + arr2
    concat.sort()
    final_result = []
    for value in concat:
        if value not in final_result:
            final_result.append(value)
    return final_result


ans = merge_arrays([1,3,5,7,9,11,12], [1,2,3,4,5,10,12])
print(ans)