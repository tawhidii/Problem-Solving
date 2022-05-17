
def uniqueId( a, n):
    result = []
    for item in a:
        if item not in result:
            result.append(item)
    return result

print(uniqueId([8, 8, 6, 2, 1],5))