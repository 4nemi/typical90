N, Q = map(int, input().split())
A = list(map(int, input().split()))

s = [0] * (N+1)
for i in range(1, N):
    s[i] = A[i] - A[i-1] 

ans = 0
for i in range(1, N):
    ans += abs(s[i])

for i in range(Q):
    L, R, V = map(int, input().split())
    pre = abs(s[L-1]) + abs(s[R])
    if L >= 2:
        s[L-1] += V
    if R < N:
        s[R] -= V
    post = abs(s[L-1]) + abs(s[R])
    ans += (post - pre)
    print(ans)