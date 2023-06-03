import sys
from collections import deque

n, k, m = map(int, sys.stdin.readline().strip().split())
edge = [[] for _ in range(n + m)]
visited = [0 for _ in range(n + m)]

for i in range(m):
    tube = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(k):
        edge[n + i].append(tube[j] - 1)
        edge[tube[j] - 1].append(n + i)

queue = deque()
queue.append(0)
visited[0] = 1
level = -1

while queue:
    station = queue.popleft()
    if station == n - 1:
        level = visited[station]
        break

    for next in edge[station]:
        if visited[next] == 0:
            queue.append(next)
            if next >= n:
                visited[next] = visited[station]
                continue
            
            visited[next] = visited[station] + 1


print(level)