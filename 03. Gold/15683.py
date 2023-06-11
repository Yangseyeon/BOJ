import sys

def set_area(idx, case):
    global cnt
    s_i, s_j = cctv[idx][1], cctv[idx][2]

    for i in range(s_i, -1, -1):
        if area[i][s_j] == 6 or case[0] == 0:
            break
        if area[i][s_j] == -idx - 1:
            area[i][s_j] = 0
            cnt += 1
        elif area[i][s_j] == 0:
            area[i][s_j] = -idx -1
            cnt -= 1

        

    for i in range(s_i, n):
        if area[i][s_j] == 6 or case[2] == 0:
            break
        if area[i][s_j] == -idx - 1:
            area[i][s_j] = 0
            cnt += 1
        elif area[i][s_j] == 0:
            area[i][s_j] = -idx-1
            cnt -= 1

       
    
    for j in range(s_j, -1, -1):
        if area[s_i][j] == 6 or case[1] == 0:
            break

        if area[s_i][j] == -idx - 1:
            area[s_i][j] = 0
            cnt += 1

        
        elif area[s_i][j] == 0:
            area[s_i][j] = -idx-1
            cnt -= 1

        

    for j in range(s_j, m):
        if area[s_i][j] == 6 or case[3] == 0:
            break
        if area[s_i][j] == -idx - 1:
            area[s_i][j] = 0
            cnt += 1
        elif area[s_i][j] == 0:
            area[s_i][j] = -idx-1
            cnt -= 1
        


def set_cctv(idx):
    global cnt
    global min_cnt
    if idx == len(cctv):
        # for i in area:
        #     print(i)
        # print(cnt)
        if cnt < min_cnt:
            min_cnt = cnt
        return
    
    for case in cctv_case[cctv[idx][0]]:
        set_area(idx, case)
        
        set_cctv(idx + 1)
        set_area(idx, case)
        

    



area = []
cctv = []
cctv_case = {
    1: [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
    2: [[1, 0, 1, 0], [0, 1, 0, 1]],
    3: [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]],
    4: [[1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1]],
    5: [[1, 1, 1, 1]]}
cnt = 0
min_cnt = 65

n, m = map(int, sys.stdin.readline().strip().split())

for i in range(n):
    area.append(list(map(int, sys.stdin.readline().strip().split())))
    for j in range(m):
        if 1<= area[i][j] <=5:
            cctv.append([area[i][j], i, j,])
        elif area[i][j] == 0:
            cnt += 1

cctv.sort()
cctv.reverse()


set_cctv(0)
print(min_cnt)