import sys

n = int(sys.stdin.readline().strip())
point_list = list()

for i in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    point_list.append([x, y])

point_list.sort()

for x, y in point_list:
    print(x, y)