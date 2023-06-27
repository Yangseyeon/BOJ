import sys
n, m = map(int, sys.stdin.readline().strip().split())
table = []
for i in range(n):
    table.append(list(map(int, sys.stdin.readline().strip().split())))
    for j in range(n):
        for x, y in [[i - 1, j], [i, j - 1], [i - 1, j - 1]]:
            if 0<= x < n and 0<= y < n:
                table[i][j] += -table[x][y] if (x == i - 1 and y == j - 1) else table[x][y]


for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    result = table[x2 - 1][y2 - 1]

    for x, y in [[x1 - 2, y1 - 2], [x2 - 1, y1 - 2], [x1 - 2, y2 - 1]]:
            if 0<= x < n and 0<= y < n:
                result += table[x][y] if (x == x1 - 2 and y == y1 - 2) else (-table[x][y])

    print(result)
