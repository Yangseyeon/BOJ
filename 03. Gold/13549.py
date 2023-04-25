import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())

visited = [0 for i in range(100001)]
queue = deque()
queue.append(n)
visited[n] = 1


while queue:
    location = queue.popleft()
    if location == k:
        print(visited[location] - 1)
        break

    next_2X = location * 2
    next_M1 = location - 1
    next_P1 = location + 1

    next_list = [location * 2, location - 1, location + 1]

    for next in next_list:
        if 0<= next <= 100000 and visited[next] == 0:
            if next == next_list[0]:
                queue.appendleft(next)
                visited[next] = visited[location]
            else:
                queue.append(next)
                visited[next] = visited[location] + 1

