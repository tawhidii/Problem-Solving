


def combo_string(a, b):
    min_ = min(len(a), len(b))
    if min_ == len(a):
        return a+b+a
    if min_ == len(b):
        return b+a+b


ans = combo_string('aaa', 'b')
print(ans)
