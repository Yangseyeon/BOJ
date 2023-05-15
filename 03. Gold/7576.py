import sys
from collections import deque
m, n = map(int, sys.stdin.readline().strip().split())
box = []
visited = [[0 for _ in range(m)] for _ in range(n)]
queue = deque()
cnt_0 = 0

for i in range(n):
    row = list(map(int, sys.stdin.readline().strip().split()))
    box.append(row)

    for j in range(m):
        if row[j] == 1:
            queue.append([i, j])
            visited[i][j] = 1

        elif row[j] == 0:
            cnt_0 += 1

level = 1

while queue:
    i, j = queue.popleft()

    for next in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
        row, col = next
        if 0<= row < n and 0<= col < m:
            if box[row][col] == 0 and visited[row][col] == 0:
                box[row][col] = 1
                visited[row][col] = visited[i][j] + 1
                level = visited[row][col]
                cnt_0 -= 1
                queue.append([row, col])


if cnt_0 == 0:
    print(level - 1)

else:
    print(-1)


