from collections import deque
import sys

n = int(sys.stdin.readline().strip())
deque_list = deque()

for i in range(n):
    func = list(sys.stdin.readline().strip().split())

    if func[0] == "push_front":
        deque_list.appendleft(int(func[1]))
    elif func[0] == "push_back":
        deque_list.append(int(func[1]))
    elif func[0] == "pop_front":
        if len(deque_list) == 0:
            print(-1)
        else:
            print(deque_list.popleft())
    elif func[0] == "pop_back":
        if len(deque_list) == 0:
            print(-1)
        else:
            print(deque_list.pop())
    elif func[0] == "size":
        print(len(deque_list))
    elif func[0] == "empty":
        if len(deque_list) == 0:
            print(1)
        else:
            print(0)
    elif func[0] == "front":
        if len(deque_list) == 0:
            print(-1)
        else:
            print(deque_list[0])
    elif func[0] == "back":
        if len(deque_list) == 0:
            print(-1)
        else:
            print(deque_list[len(deque_list) - 1])
