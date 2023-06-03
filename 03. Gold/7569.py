import sys
from collections import deque
m, n, h = map(int, sys.stdin.readline().strip().split())
box = [[] for _ in range(h)]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
queue = deque()
cnt0 = 0

for i in range(h):
    for j in range(n):
        box[i].append(list(map(int, sys.stdin.readline().strip().split())))
        

        for k in range(m):
            if box[i][j][k] == 1:
                visited[i][j][k] = 1
                queue.append([i, j, k])

            elif box[i][j][k] == 0:
                cnt0 += 1

level = -1

while queue:
    i, j, k = queue.popleft()

    if level < visited[i][j][k]:
        level = visited[i][j][k]

    for x, y, z in [[i + 1, j, k], [i - 1, j, k], [i, j - 1, k], [i, j + 1, k], [i, j, k - 1], [i, j, k + 1]]:
        if 0<= x < h and 0<= y <n and 0<= z < m:
            if visited[x][y][z] == 0 and box[x][y][z] == 0:
                visited[x][y][z] = visited[i][j][k] + 1
                box[x][y][z] = 1
                cnt0 -= 1
                queue.append([x, y, z])

if cnt0 == 0:
    print(level - 1)

else:
    print(-1)