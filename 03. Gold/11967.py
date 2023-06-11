import sys
from collections import deque
n, m = map(int, sys.stdin.readline().strip().split())
room = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, a, b = map(int, sys.stdin.readline().strip().split())
    room[x - 1][y - 1].append([a - 1, b - 1])

q = deque()

road = [[0 for _ in range(n)] for _ in range(n)]
light = [[0 for _ in range(n)] for _ in range(n)]

q.append([0, 0])
light[0][0] = 1
road[0][0] = 1
cnt = 1

while q:
    i, j = q.popleft()
    
    for x, y in room[i][j]:
        if light[x][y] == 0:
            light[x][y] = 1
            cnt += 1

        for prex, prey in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
            if 0<= prex< n and 0<= prey < n:
                if road[x][y] == 0 and road[prex][prey] == 1:
                    road[x][y] = 1
                    q.append([x, y])
                    break

    for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
        if 0<= x< n and 0<= y < n:
            if light[x][y] == 1 and road[x][y] == 0:
                road[x][y] = 1
                q.append([x, y])

            
print(cnt)