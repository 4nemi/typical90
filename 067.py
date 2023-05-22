N, K = map(int, input().split())

def toten(n):
    r = 0
    n = str(n)[::-1]
    for i in range(len(n)):
        r += int(n[i]) * (8**i)
    return r 

def tonine(n):
    if n == 0:
        return 0
    r = ''
    while n > 0:
        if n%9 != 8:
            r += str(n%9)
        else:
            r += '5'
        n //= 9
    return int(r[::-1])

for i in range(K):
    N = toten(N)
    N = tonine(N)

print(N)
