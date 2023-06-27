import sys
from collections import deque

def check_land_divided(level):
    if not land:
        return True

    q = deque()
    q.append(land[0])
    visited[land[0][0]][land[0][1]] = level
    cnt = 1

    while q:
        i, j = q.popleft()

        for x, y in [[i - 1 , j], [i, j - 1], [i, j + 1], [i + 1, j]]:
            if 0<= x < n and 0<= y < m:
                if area[x][y] != 0 and visited[x][y] == level - 1:
                    visited[x][y] = level
                    q.append([x, y])
                    cnt += 1

    return False if cnt == len(land) else True


def melting_land():
    global land
    level = 0

    while land:
        update_land = []
        remove_land = []

        for i, j in land:
            cnt = 0
            for x, y in [[i - 1 , j], [i, j - 1], [i, j + 1], [i + 1, j]]:
                if 0<= x < n and 0<= y < m:
                    if area[x][y] == 0:
                        cnt += 1
            

            if area[i][j] > cnt:
                area[i][j] = area[i][j] - cnt
                update_land.append([i, j])
                
            else:
                remove_land.append([i, j])

        land = update_land
        for i, j in remove_land:
            area[i][j] = 0
        
        level += 1
        if check_land_divided(level):
            break

    if not land:
        level = 0
    print(level)


n, m = map(int, sys.stdin.readline().strip().split())
area = []
land = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    area.append(list(map(int, sys.stdin.readline().strip().split())))
    for j in range(m):
        if area[i][j] != 0:
            land.append([i, j])

melting_land()
