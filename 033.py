H, W = map(int, input().split())

if H != 1 and W != 1:
    if H % 2 == 0:
        A = H // 2
    else:
        A = H // 2 + 1

    if W % 2 == 0:
        B = W // 2
    else: 
        B = W // 2 + 1
else:
    A = H
    B = W

print(A * B)