import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())

visited = [0 for i in range(100001)]
queue = deque()
queue.append(n)
visited[n] = 1
cnt = 0
min = 0


while queue:
    location = queue.popleft()
    
    if visited[location] > min and cnt != 0:
        continue

    if location == k:
        if cnt == 0:
            min = visited[location]
        cnt += 1
        continue
        

    next_list = [location * 2, location - 1, location + 1]

    for next in next_list:
        if 0<= next <= 100000:
            if visited[next] == 0 or visited[next] == visited[location] + 1:
                queue.append(next)
                visited[next] = visited[location] + 1

print(min - 1)
print(cnt)
