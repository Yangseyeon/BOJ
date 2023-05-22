import sys
from collections import deque

n, k, m = map(int, sys.stdin.readline().strip().split())

edge = [[] for _ in range(n)]

for _ in range(m):
    s_list = list(map(int, sys.stdin.readline().strip().split()))

    for i in s_list:
        for j in s_list:
            if j - 1 not in edge[i - 1] and i - 1 != j - 1:
                edge[i - 1].append(j - 1)


visited = [0 for _ in range(n)]
queue = deque()
queue.append(0)
visited[0] = 1
level = -1

while queue:
    vertice = queue.popleft()
    if vertice == n - 1:
        level = visited[vertice]

    for v in edge[vertice]:
        if visited[v] == 0:
            queue.append(v)
            visited[v] = visited[vertice] + 1

print(level)
