import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().strip().split())

edge =[[] for _ in range(n)]
visited = [0 for _ in range(n)]
route_dfs = [v]
route_bfs = [v]
visited[v - 1] = 1

def dfs(idx):
    for i in sorted(edge[idx]):
        if visited[i] == 1:
            continue
        route_dfs.append(i + 1)
        visited[i] = 1
        dfs(i)

def bfs(v):
    queue = deque()
    visited = [0 for _ in range(n)]
    queue.append(v)
    visited[v] = 1

    while queue:
        idx = queue.popleft()

        for i in sorted(edge[idx]):
            if visited[i] == 1:
                continue
            route_bfs.append(i + 1)
            queue.append(i)
            visited[i] = 1


for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    edge[v1 - 1].append(v2 - 1)
    edge[v2 - 1].append(v1 - 1)

dfs(v - 1)
bfs(v - 1)
print(*route_dfs)
print(*route_bfs)
