from math import gcd

A, B = map(int, input().split())

g = gcd(A, B)
a = A // g
b = B // g
ans = a * b * g
if ans > 10 ** 18:
    print('Large')
else:
    print(ans)