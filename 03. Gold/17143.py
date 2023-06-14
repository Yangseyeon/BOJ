import sys

def next_area(key):
    row, col, s, d = shark[key]
    if area[row - 1][col - 1] == key:
        area[row - 1][col - 1] = -1

    if d == 1:
        if s > row - 1:
            s = s - (row - 1)
            div = s // (r - 1)
            mod = s % (r - 1)

            if div % 2 == 0:
                shark[key][0] = 1 + mod
                shark[key][3] = 2
            else:
                shark[key][0] = r - mod
                
        else:
            shark[key][0] = row - s


    if d == 2:
        if row + s > r - 1:
            s = s - (r - row)
            div = s // (r - 1)
            mod = s % (r - 1)

            if div % 2 == 0:
                shark[key][0] = r - mod
                shark[key][3] = 1
            else:
                shark[key][0] = 1 + mod
                

        else:
            shark[key][0] = row + s

    if d == 3:
        if col + s > c - 1:
            s = s - (c - col)
            div = s // (c - 1)
            mod = s % (c - 1)

            if div % 2 == 0:
                shark[key][1] = c - mod
                shark[key][3] = 4
            else:
                shark[key][1] = 1 + mod

        else:
            shark[key][1] = col + s

    if d == 4:
        if s > col - 1:
            s = s - (col - 1)
            div = s // (c - 1)
            mod = s % (c - 1)

            if div % 2 == 0:
                shark[key][1] = 1 + mod
                shark[key][3] = 3
            else:
                shark[key][1] = c - mod

        else:
            shark[key][1] = col - s

    if area[shark[key][0] - 1][shark[key][1] - 1] < key:
        area[shark[key][0] - 1][shark[key][1] - 1] = key
        return True
    return False

def move_shark(k):
    global shark_key
    new_key = []

    for key in shark_key:
        if key == k:
            continue
        if next_area(key):
            new_key.append(key)
    
    
    shark_key = new_key


def catch_shark(key):
    area[shark[key][0] - 1][shark[key][1] - 1] = -1
    return key


def fishing():
    result = 0
    for j in range(c):
        key = -1
        for i in range(r):
            if area[i][j] != -1:
                key = area[i][j]
                result += catch_shark(area[i][j])
                break
        
        move_shark(key)

    return result

r, c, m = map(int, sys.stdin.readline().strip().split())
shark = {}
shark_key = []
area = [[-1 for _ in range(c)] for _ in range(r)]

for i in range(m):
    r_s, c_s, s, d, z = map(int, sys.stdin.readline().strip().split())
    shark[z] = [r_s, c_s, s, d]
    area[r_s - 1][c_s - 1] = z
    shark_key.append(z)

shark_key.sort()
shark_key.reverse()

print(fishing())
