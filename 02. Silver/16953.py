import sys
from collections import deque

A, B = map(int, sys.stdin.readline().strip().split())
queue = deque()
visited = deque()
queue.append(A)
visited.append(1)
flag = 0

while queue:
    #print(queue)
    num = queue.popleft()
    level = visited.popleft()
    if num == B:
        flag = 1
        print(level)
        break

    next_num = [num * 2, num * 10 + 1]
    for n in next_num:
        if n > B:
            continue

        queue.append(n)
        visited.append(level + 1)


if flag == 0:
    print(-1)