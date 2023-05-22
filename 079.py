H, W = map(int, input().split())

A = []
B = []

for i in range(H):
    A.append(list(map(int, input().split())))
for i in range(H):
    B.append(list(map(int, input().split())))

cnt = 0
for i in range(H-1):
    for j in range(W-1):
        v = B[i][j] - A[i][j]
        if v != 0:
            A[i][j] += v
            A[i+1][j] += v
            A[i][j+1] += v
            A[i+1][j+1] += v
            cnt += abs(v)

flag = True
for i in range(H):
    if A[i][W-1] != B[i][W-1]:
        flag = False
for i in range(W):
    if A[H-1][i] != B[H-1][i]:
        flag = False

if flag:
    print('Yes')
    print(cnt)
else:
    print('No')