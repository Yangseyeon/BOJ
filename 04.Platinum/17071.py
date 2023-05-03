import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())

queue = deque()
queue.append(n)
visited = [[False]*500001 for _ in range(2)]
visited[0][n] = True
flag = 0
level = 0
l = -1
while len(queue) != 0:
    if k > 500000: break
    if visited[flag][k]:
        l = level
        break

    tmp = deque()
    flag = 1 - flag
    while len(queue) != 0:
        x = queue.popleft()
        for i in (x-1, x+1, x*2):
            if 0 <= i <= 500000 and not visited[flag][i]:
                visited[flag][i] = True
                tmp.append(i)
                    
    level += 1
    k += level
    queue = tmp
    
print(l)