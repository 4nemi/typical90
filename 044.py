N, Q = map(int, input().split())
A = list(map(int, input().split()))

def change(A, x, y):
    A[x-1], A[y-1] = A[y-1], A[x-1]
    return A

def ans(A, x):
    return A[x-1]

sift_count = 0
for _ in range(Q):
    T, x, y = map(int, input().split())
    x = (x-sift_count) % N
    y = (y-sift_count) % N
    if T == 1:
        A = change(A, x, y)
    elif T == 2:
        sift_count += 1
    elif T == 3:
        print(ans(A, x))