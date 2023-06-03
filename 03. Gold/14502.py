import sys
import copy
from collections import deque
n, m = map(int, sys.stdin.readline().strip().split())
area_cp = []
wall = []
virus = []

for i in range(n):
    area_cp.append(list(map(int, sys.stdin.readline().strip().split())))
    for j in range(m):
        if area_cp[i][j] == 0:
            wall.append([i, j])
        
        elif area_cp[i][j] == 2:
            virus.append([i, j])


wall_set = []

for i in range(len(wall) - 2):
    for j in range(i + 1, len(wall) - 1):
        for k in range(j + 1, len(wall)):
            wall_set.append([wall[i], wall[j], wall[k]])


def bfs():

    max_area = -1
    wall_size = len(wall) - 3

    for w in wall_set:
        virus_cnt = 0
        area = copy.deepcopy(area_cp)
        area[w[0][0]][w[0][1]] = 1
        area[w[1][0]][w[1][1]] = 1
        area[w[2][0]][w[2][1]] = 1
        
        virus_q = deque(virus)
        while virus_q:
            i, j = virus_q.popleft()

            for next_i, next_j in [[i - 1 , j], [i, j - 1], [i, j + 1], [i + 1, j]]:
                if 0<= next_i < n and 0<= next_j < m:
                    if area[next_i][next_j] == 0:
                        area[next_i][next_j] = 2
                        virus_cnt += 1
                        virus_q.append([next_i, next_j])

        if wall_size - virus_cnt > max_area:
            max_area = wall_size - virus_cnt


    print(max_area)

bfs()