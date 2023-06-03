import sys
from collections import deque
queue = deque()
chicken =  []
house = []
n, m = map(int, sys.stdin.readline().strip().split())
city = []

for i in range(n):
    city.append(list(map(int, sys.stdin.readline().strip().split())))
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i, j])

print(city)
print(chicken)
