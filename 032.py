#pypy3
from itertools import permutations
N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
M = int(input())
kenaku = [[False] * (N+1) for _ in range(N+1)]
for i in range(M):
    X, Y = map(int, input().split())
    kenaku[X][Y] = True
    kenaku[Y][X] = True

ans = 10**18
for interval in permutations(range(1, N+1)):
    run = 0
    flag = True
    for i in range(N):
        run += A[interval[i]-1][i]
        if i < N-1 and kenaku[interval[i]][interval[i+1]]:
            flag = False
    if flag:
        ans = min(ans, run)

if ans < 10**4:
    print(ans)
else:
    print('-1')