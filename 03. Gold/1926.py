import sys
from collections import deque
n, m = map(int, sys.stdin.readline().strip().split())
paper = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

max_pic = 0
pic_cnt = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and paper[i][j] == 1:
            q = deque([[i, j]])
            visited[i][j] = 1
            cnt = 0

            while q:
                x, y = q.popleft()
                cnt += 1

                for n_X, n_y in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                    if 0<= n_X < n and 0<= n_y < m:
                        if visited[n_X][n_y] == 0 and paper[n_X][n_y] == 1:
                            visited[n_X][n_y] = 1
                            q.append([n_X, n_y])

            max_pic = max(max_pic, cnt)
            pic_cnt += 1


print(pic_cnt)
print(max_pic)



