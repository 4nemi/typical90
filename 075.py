N = int(input())

#Nに含まれる素因数の個数を数える
def count_prime(n):
    count = 0
    for i in range(2, int(n**0.5)+1):
        while n%i == 0:
            n //= i
            count += 1
    if n != 1:
        count += 1
    return count

cnt = count_prime(N)

if cnt == 1:
    print(0)
else:
    x = 1
    while 2**x < cnt:
        x += 1
    print(x)