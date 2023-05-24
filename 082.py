L, R = map(int, input().split())

left_digit = len(str(L))-1
right_digit = len(str(R))-1

ans = 0
l = L
for i in range(left_digit, right_digit+1):
    r = 10**(i+1) - 1
    if r > R:
        tmp = ((R+1)*R // 2 - l*(l-1) // 2) * (i+1)
    else:
        tmp = ((r+1)*r // 2 - l*(l-1) // 2) * (i+1)
    ans += tmp % (10 ** 9 + 7)
    l = 10 ** (i+1)

print(ans%(10**9+7))