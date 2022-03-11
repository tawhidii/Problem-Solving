def make_tags(tag, word):
    return "<{0}>{1}</{2}>".format(tag, word, tag)


ans = make_tags('i', 'Yay')
print(ans)
