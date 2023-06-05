import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().strip().split())
que = deque()
visited = [0 for _ in range(f + 1)]

que.append(s)
visited[s] = 1
level = "use the stairs"

while que:
    floor = que.popleft()
    if floor == g:
        level = str(visited[floor] - 1)
        break

    for next in [floor + u, floor - d]:
        if 1<= next <= f:
            if visited[next] == 0:
                visited[next] = visited[floor] + 1
                que.append(next)


print(level)