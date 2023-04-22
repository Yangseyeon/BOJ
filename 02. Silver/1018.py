import sys
n, m = map(int, sys.stdin.readline().strip().split())

puzzle = list()
min = 65

for _ in range(n):
    puzzle.append(sys.stdin.readline().strip())


for i in range(n - 7):
    for j in range(m - 7):
        black_even = 0
        white_even = 0
        black_odd = 0
        white_odd = 0
        for row in range(i, i + 8):
            for col in range(j, j + 8):
                if (row % 2 == 0 and col % 2 ==0) or (row % 2 == 1 and col % 2 ==1):
                    if puzzle[row][col] == "W":
                        white_even += 1
                    else:
                        black_even += 1
                else:
                    if puzzle[row][col] == "W":
                        white_odd += 1
                    else:
                        black_odd += 1

        if black_even+ white_odd < black_odd+ white_even:
            tmp = black_even+ white_odd
        else:
            tmp = black_odd+ white_even
        # print(tmp)
        
        if tmp < min:
            min = tmp

print(min)