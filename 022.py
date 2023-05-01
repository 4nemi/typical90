A, B, C = map(int, input().split())
A_, B_, C_ = A, B, C

#AとBの最大公約数
while A != 0 and B != 0:
    if A > B:
        A %= B
    else:
        B %= A

    if A == 0:
        gcd = B
    if B == 0:
        gcd = A

#Cとgcdの最大公約数
while C != 0 and gcd != 0:
    if C > gcd:
        C %= gcd
    else:
        gcd %= C

    if C == 0:
        r = gcd
    if gcd == 0:
        r = C

print((A_//r -1) + (B_//r -1) + (C_//r -1)) 