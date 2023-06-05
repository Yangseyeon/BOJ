import sys
[print(i[0], i[1]) for i in sorted(list(map(int, sys.stdin.readline().strip().split())) for _ in range(int(sys.stdin.readline().strip())))]