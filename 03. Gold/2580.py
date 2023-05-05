import sys
puzzle = []
zero = []

def is_correct_num(row, col, num):
    if num in puzzle[row]:
        return False
    
    for i in range(9):
        if num == puzzle[i][col]:
            return False
    
    r = (row // 3) * 3
    c = (col //3) *3

    for i in range(3):
        for j in range(3):
            if num == puzzle[r + i][c + j]:
                return False
    
    return True


def mk_puzzle(row):
    if row == len(zero):
        for r in puzzle:
            print(*r)
        exit(0)

    for j in range(1, 10):
        if is_correct_num(zero[row][0], zero[row][1], j) == False:
            continue
        puzzle[zero[row][0]][zero[row][1]] = j
        mk_puzzle(row + 1)
        puzzle[zero[row][0]][zero[row][1]] = 0

def main():
    for i in range(9):
        puzzle.append(list(map(int, sys.stdin.readline().strip().split())))
        for j in range(9):
            if puzzle[i][j] == 0:
                zero.append([i, j])

    mk_puzzle(0)
    


if __name__ == "__main__":
    main()