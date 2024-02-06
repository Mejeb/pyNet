MOD = 998244353


def power(x, y):
    res = 1
    while y > 0:
        if y & 1:
            res = res * x % MOD
        x = x * x % MOD
        y >>= 1
    return res

N, M = map(int, input().split())
S = [input().strip() for _ in range(M)]


dp = [[0]*(N+10) for _ in range(M+1)]
dp[0][0] = 1


for i in range(1, M+1):
    for j in range(N, 0, -1):
        for k in range(1, j+1):
            if k >= len(S[i-1]):
                dp[i][j] = (dp[i][j] + dp[i-1][j-len(S[i-1])]*power(26, len(S[i-1]))) % MOD
            else:
                dp[i][j] = (dp[i][j] + dp[i][j-len(S[i-1])]) % MOD

total = power(26, N)
for i in range(1, M+1):
    total = (total - dp[i][N]*power(2, i)%MOD + MOD) % MOD

print(total)
