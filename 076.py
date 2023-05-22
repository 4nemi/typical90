from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

if sum(A) % 10 != 0:
    print('No')
    exit()

p = sum(A) // 10
X = A + A

s = [0] * (N*2)
s[0] = X[0]
for i in range(N*2-1):
    s[i+1] = s[i] + X[i+1]

#print(s)

for i in range(N):
    q = s[i] + p
    j = bisect_left(s, q)
    if s[j] == q:
        print('Yes')
        exit()

print('No')