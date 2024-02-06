MOD = 998244353
N, M = map(int, input().split())
S = [input().strip() for _ in range(M)]

sikuIle = [1]
for _ in range(N+10):
    sikuIle.append(sikuIle[-1]*2%MOD)


moyaIvi = [1]
for _ in range(N+10):
    moyaIvi.append(moyaIvi[-1]*26%MOD)


ataVile = [0]*(N+10)
ataVile[0] = 1


for s in S:
    m = len(s)
    ataVile1 = ataVile[:]
    for i in range(m, N+1):
        ataVile[i] = (ataVile[i] + ataVile1[i-m]*sikuIle[m-1]) % MOD
    for i in range(1, N+1):
        ataVile[i] = (ataVile[i] + ataVile[i-1]) % MOD

total = moyaIvi[N]
for i in range(1, N+1):
    total = (total - moyaIvi[N-i]*ataVile[i]%MOD + MOD) % MOD

print(total)
