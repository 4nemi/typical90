from itertools import product

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

S = 1
for i in range(N):
    S *= sum(A[i])

print(S % (10**9 + 7))
