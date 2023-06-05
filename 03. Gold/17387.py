import sys


x1, y1, x2, y2 = map(int, sys.stdin.readline().strip())
x3, y3, x4, y4 = map(int, sys.stdin.readline().strip())
case1 = 0
case2 = 0

# x축과 수직일 때 x1 - x2 == 0
if x1 - x2 == 0:
    case1 = 1
# y축과 수직일 때 y1 - y2 == 0
elif y1 - y2 == 0:
    case1 = 2
# x1 - x2 != 0 y1 - y2 != 0
else:
    case1 = 3

# x축과 수직일 때 x1 - x2 == 0
if x3 - x4 == 0:
    case1 = 1
# y축과 수직일 때 y1 - y2 == 0
elif y3 - y4 == 0:
    case2 = 2
# x1 - x2 != 0 y1 - y2 != 0
else:
    case2 = 3

ans = 0
if case1 == 1 and case2 == 1:
    if x1 == x3:
        min(y1, y2) <= max(y3, y4)


