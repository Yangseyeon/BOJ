import sys
from collections import deque

n = int(sys.stdin.readline().strip())
area = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
visited_from = [[[0, 0] for _ in range(n)] for _ in range(n)]
area_end = deque()

#섬 영역 나누기
def indexing_area():
    area_cnt = 2
    for i in range(n):
        for j in range(n):
            if area[i][j] == 0 or visited[i][j] == 1:
                visited[i][j] = 1
                continue

            queue = deque()
            queue.append([i, j])
            visited[i][j] = 1

            while queue:
                row, col = queue.popleft()
                area[row][col] = area_cnt
                visited[row][col] = 1

                cnt = 0

                if row > 0:
                    if area[row - 1][col] == 0:
                        cnt += 1

                if col < n - 1:
                    if area[row][col + 1] == 0:
                        cnt += 1

                if col > 0:
                    if area[row][col - 1] == 0:
                        cnt += 1
                if row < n-1:
                    if area[row + 1][col] == 0:
                        cnt += 1

                if cnt > 0:
                    area_end.append([row, col])
                    visited_from[row][col] = [area_cnt, 0]



                for next in [[row, col + 1],[row - 1, col], [row, col - 1],[row + 1, col]]:
                    if 0<= next[0] < n and 0<= next[1] < n:
                        if visited[next[0]][next[1]] == 0 and area[next[0]][next[1]] == 1:
                            queue.append(next)
                            visited[next[0]][next[1]] = 1

            area_cnt += 1



def bfs():
    min = 10000
    flag = 0
    while area_end:
        row, col = area_end.popleft()
        if flag == 1 and min < visited_from[row][col][1] * 2:
            break

        for next in [[row - 1, col], [row, col + 1], [row, col - 1],[row + 1, col]]:
            i, j = next
            if 0<= i < n and 0<= j < n:
                if visited_from[i][j][0] == 0 and area[i][j] == 0:
                    area_end.append([i, j])
                    visited_from[i][j] = [visited_from[row][col][0], visited_from[row][col][1] + 1]
                    continue

                if visited_from[i][j][0] != 0 and visited_from[i][j][0] != visited_from[row][col][0]:
                    flag = 1
                    if min > visited_from[row][col][1] + visited_from[i][j][1]:
                        min = visited_from[row][col][1] + visited_from[i][j][1]

    if flag == 0:
        print(0)
    else:
        print(min)
                    

indexing_area()
bfs()
