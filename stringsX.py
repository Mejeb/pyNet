MOD = 998244353

# Function to calculate x^y under modulo MOD
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

# Initialize dynamic programming table
dp = [[[0]*(N+10) for _ in range(M+1)] for _ in range(M+1)]
for i in range(M+1):
    for j in range(N+10):
        dp[i][j][0] = 1

# Calculate number of occurrences of each string Si
for i in range(1, M+1):
    for j in range(N, 0, -1):
        for k in range(1, j+1):
            if k >= len(S[i-1]):
                dp[i][j][k] = (dp[i][j][k] + dp[i-1][j-len(S[i-1])][k]*power(26, len(S[i-1]))) % MOD
            else:
                dp[i][j][k] = (dp[i][j][k] + dp[i][j][k-1]) % MOD

# Calculate total power
total = power(26, N)
for i in range(1, M+1):
    total = (total - dp[i][N][i]*power(2, i)%MOD + MOD) % MOD

print(total)
