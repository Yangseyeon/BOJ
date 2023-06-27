import sys
sys.setrecursionlimit(10**9)

def dfs(i, j):
    if [i, j] == [n - 1, m - 1]:
        dp[i][j] = 1
        return
    if dp[i][j] != -1:
        return
    
    dp[i][j] = 0
    for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
        if 0<= x < n and 0<= y < m:
            if area[i][j] > area[x][y]:
                dfs(x, y)
                dp[i][j] += dp[x][y]

n, m = map(int, sys.stdin.readline().strip().split())
area = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]

dfs(0,0)
print(dp[0][0])
