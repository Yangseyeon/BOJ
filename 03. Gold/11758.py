import sys

vertices = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(3)]

result = (vertices[1][0] - vertices[0][0]) * (vertices[2][1] - vertices[1][1]) - (vertices[2][0] - vertices[1][0])  * (vertices[1][1] - vertices[0][1])

if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)