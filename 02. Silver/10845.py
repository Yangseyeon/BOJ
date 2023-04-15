from collections import deque
import sys

dq = deque()
n = int(sys.stdin.readline().strip())

for i in range(n):
    func = list(sys.stdin.readline().strip().split())

    if func[0] == "push":
        dq.appendleft(int(func[1]))
    elif func[0] == "pop":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif func[0] == "size":
        print(len(dq))
    elif func[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif func[0] == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif func[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[len(dq) - 1])