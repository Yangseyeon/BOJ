import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
island = []
land = []

for i in range(n):
    island.append(sys.stdin.readline().strip())

    for j in range(m):
        if island[i][j] == "L":
            land.append([i, j])
        
max = -1
for x, y in land:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()

    queue.append([x, y])
    visited[x][y] = 1

    while queue:
        r, c = queue.popleft()

        if visited[r][c] > max:
            max = visited[r][c]


        for i, j in [[r - 1, c], [r + 1, c], [r, c- 1], [r, c + 1]]:
            if 0<= i < n and 0<= j < m:
                if visited[i][j] == 0 and island[i][j] == "L":
                    queue.append([i, j])
                    visited[i][j] = visited[r][c] + 1

    
    # for row in visited:
    #     print(*row)
    # print()


print(max - 1)
