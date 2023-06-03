import sys
from collections import deque

n = int(sys.stdin.readline().strip())

for _ in range(n):
    func = sys.stdin.readline().strip()
    size = int(sys.stdin.readline().strip())
    queue = deque(sys.stdin.readline().strip()[1:-1].split(","))

    method = [queue.popleft, queue.pop]

    flag = 0
    err = 0
    for f in func:
        if f == "R":
            flag = 1 - flag

        if f == "D":
            if len(queue) == 0 or size == 0:
                print("error")
                err = 1
                break
            method[flag]()

    if err == 1:
        continue
    
    if flag == 1:
        queue.reverse()
    print("["+",".join(list(queue))+"]")
        



