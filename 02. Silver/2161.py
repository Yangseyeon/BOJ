from collections import deque
num =deque([i for i in range(1, int(input()) + 1)])
while num:
    print(num.popleft(), end = " ")
    if num:
        num.append(num.popleft())
