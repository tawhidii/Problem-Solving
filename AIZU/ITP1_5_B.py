
# while True:
#     H, W = map(int, input().split())
#     if H == 0 and W == 0:
#         break

#     for i in range(H):
#         for j in range(W):
#             if i == 0 or i == H-1 or j == 0 or j == W-1:
#                 print('#', end='')
#             else:
#                 print('.', end='')
#         print()
#     print()


for i in range(3):
    for j in range(4):
        print(i, j)
