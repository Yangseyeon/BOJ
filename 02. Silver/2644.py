import sys
from collections import deque

n = int(sys.stdin.readline().strip())
p1, p2 = map(int, sys.stdin.readline().strip().split())
m = int(sys.stdin.readline().strip())

family = [[] for _ in range(n)]
visited = [0 for _ in range(n)]

for _ in range(m):
    pa, pb = map(int, sys.stdin.readline().strip().split())
    family[pa - 1].append(pb - 1)
    family[pb - 1].append(pa - 1)

level = -1
queue = deque()

queue.append(p1 - 1)
visited[p1 - 1] = 1

while queue:
    p = queue.popleft()

    if p == p2 - 1:
        level = visited[p] - 1
        break

    for i in family[p]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = visited[p] + 1


print(level)
