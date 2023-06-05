import sys
from collections import deque
n, m = map(int, sys.stdin.readline().strip().split())
road = [sys.stdin.readline().strip() for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

que = deque()
que.append([0, 0])
visited[0][0] = 1
while que:
    i, j = que.popleft()

    if i == n - 1 and j == m - 1:
        print(visited[i][j])
        break

    for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
        if 0<= x < n and 0<= y < m:
            if visited[x][y] == 0 and road[x][y] == "1":
                que.append([x, y])
                visited[x][y] = visited[i][j] + 1

