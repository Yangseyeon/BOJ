import sys
from collections import deque

def bfs(i, j):
    q = deque()
    q.append([i, j])
    area1[i][j] = level
    rgb = picture[i][j]

    while q:
        x, y = q.popleft()

        for n_x, n_y in [[x + 1, y], [x - 1, y], [x, y - 1], [x, y + 1]]:
            if 0<= n_x < n and 0<= n_y <n:
                if area1[n_x][n_y] == 0 and picture[n_x][n_y] == rgb:
                    area1[n_x][n_y] = level
                    q.append([n_x, n_y])


def bfs2(i, j):
    q = deque()
    q.append([i, j])
    area2[i][j] = level2

    if picture[i][j] == "B":
        rgb = ["B"]
    else:
        rgb = ["R", "G"]

    while q:
        x, y = q.popleft()

        for n_x, n_y in [[x + 1, y], [x - 1, y], [x, y - 1], [x, y + 1]]:
            if 0<= n_x < n and 0<= n_y <n:
                if area2[n_x][n_y] == 0 and picture[n_x][n_y] in rgb:
                    area2[n_x][n_y] = level2
                    q.append([n_x, n_y])



n = int(sys.stdin.readline().strip())
picture = [sys.stdin.readline().strip() for _ in range(n)]

area1 = [[0 for _ in range(n)] for _ in range(n)]
area2 = [[0 for _ in range(n)] for _ in range(n)]
level = 0
level2 = 0

for i in range(n):
    for j in range(n):
        if area1[i][j] == 0:
            level += 1
            bfs(i, j)

        if area2[i][j] == 0:
            level2 += 1
            bfs2(i, j)


print(level, level2)