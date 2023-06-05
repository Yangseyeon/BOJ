import sys
from collections import deque
n = sys.stdin.readline().strip()
numbers = list(map(int, sys.stdin.readline().strip().split()))
stack = []
result = deque()
for num in numbers:
    while len(stack):
        if stack[-1] <= num:
            stack.pop()
        else:
            result.appendleft(stack[-1])
            break
    if len(stack) == 0:
        result.appendleft(-1)

print(*list(result))