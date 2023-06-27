import sys
sys.setrecursionlimit(10**9)

def dfs(i, j):
    visited[i][j] = 1
    next = []
    for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
        if 0<= x < n and 0<= y < n:
            if area[x][y] < area[i][j]:
                if visited[x][y] == 0:
                    dfs(x, y)
                next.append(visited[x][y])
    
    if next:
        visited[i][j] += max(next)

n = int(sys.stdin.readline().strip())
area = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
max_visit = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)
            max_visit = max(max_visit, visited[i][j])

print(max_visit)