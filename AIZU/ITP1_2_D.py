W, H, x, y, r = map(int, input().split())
if (x+r) > W or (x-r) < 0 or (y+r) > H or (y-r) < 0 or x < 0 or y < 0:
    print("No")
else:
    print("Yes")
