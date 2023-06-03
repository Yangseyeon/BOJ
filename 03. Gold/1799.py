import sys
n = int(sys.stdin.readline().strip())
puzzle = []
bishop_area = []

for i in range(n):
    puzzle.append(list(map(int, sys.stdin.readline().strip().split())))

    for j in range(n):
        if puzzle[i][j] == 1:
            bishop_area.append([i,j])

max_cnt = -1

def check_area(row, col):
    for i in range(1, row + 1):
        if row - i >= 0 and col - i >= 0:
            if puzzle[row - i][col - i] == 2:
                return False
            

        if row - i >= 0 and col + i < n:
            if puzzle[row - i][col + i] == 2:
                return False
            
    return True

def find_bishop_case(area_idx, cnt):
    if area_idx == len(bishop_area):
        global max_cnt
        if cnt > max_cnt:
            max_cnt = cnt
        return
    
    for idx in range(area_idx, len(bishop_area)):
        
        i = bishop_area[idx][0]
        j = bishop_area[idx][1]

        if check_area(i, j) == True:
            puzzle[i][j] = 2
            find_bishop_case(idx + 1, cnt + 1)
            puzzle[i][j] = 1

find_bishop_case(0, 0)
print(max_cnt)
    

    

