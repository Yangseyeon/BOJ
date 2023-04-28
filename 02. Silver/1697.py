import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())

visited = [0 for i in range(100001)]
visit_from = [0 for i in range(100001)]
queue = deque()
queue.append(n)
visited[n] = 1
root = []

while queue:
    location = queue.popleft()

    if location == k:
        print(visited[location] - 1)

        break
        

    next_list = [location * 2, location - 1, location + 1]

    for next in next_list:
        if 0<= next <= 100000:
            if visited[next] == 0:
                queue.append(next)
                visit_from[next] = location
                visited[next] = visited[location] + 1
