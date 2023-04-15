size = int(input())
puzzle = [0 for i in range(size)]
cnt = 0

def is_correct_col(row, col):
    idx = 1
    while row - idx >= 0:
        if puzzle[row - idx] == col - idx or puzzle[row - idx] == col + idx or puzzle[row - idx] == col:
            return False
        idx += 1
    return True

def find_n_queen(row):
    global cnt
    if row == size:
        cnt += 1
        return
    for col in range(size):
        if is_correct_col(row, col) == True:
            puzzle[row] = col
            find_n_queen(row + 1)
            
find_n_queen(0)
print(cnt)