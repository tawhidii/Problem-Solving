def string_match(a, b):
    min_len = min(len(a), len(b))
    count = 0
    for i in range(min_len-1):
        a_sub_str = a[i:i+2]
        b_sub_str = b[i:i+2]
        if a_sub_str == b_sub_str:
            count += 1
    return count


ans = string_match('xxcaazz', 'xxbaaz')
print(ans)
