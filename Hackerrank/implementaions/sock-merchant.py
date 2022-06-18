


def sockMerchant(n, ar):
    # Write your code here
    pairs = 0
    for ele in set(ar):
        pairs += ar.count(ele) // 2
    return pairs




sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20])

 