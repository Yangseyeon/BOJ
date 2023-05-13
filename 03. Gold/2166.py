import sys
n = int(sys.stdin.readline().strip())

x1, y1 = map(int, sys.stdin.readline().strip().split())
x2, y2 = map(int, sys.stdin.readline().strip().split())
S = 0

for _ in range(n - 2):
    x3, y3 = map(int, sys.stdin.readline().strip().split())
    S += ((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)) / 2.0
    x2, y2 = x3, y3

print("%.1f" % abs(S))