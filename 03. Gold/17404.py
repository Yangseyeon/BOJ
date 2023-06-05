import sys
INF = 1000*1000+1
n = int(sys.stdin.readline().strip())
first = list(map(int, sys.stdin.readline().strip().split()))
RGB = [[first[0], INF, INF], [INF, first[1], INF], [INF, INF, first[2]]]

for _ in range(n - 1):
    r, g, b = map(int, sys.stdin.readline().strip().split())

    for i in range(3):
        RGB[i] = [
            min(RGB[i][1], RGB[i][2]) + r, 
            min(RGB[i][0], RGB[i][2]) + g,
            min(RGB[i][0], RGB[i][1]) + b
        ]

print(min(RGB[0][1], RGB[0][2],RGB[1][0], RGB[1][2], RGB[2][0], RGB[2][1]))

