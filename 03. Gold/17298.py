import sys
from collections import deque
n = sys.stdin.readline().strip()
numbers = list(map(int, sys.stdin.readline().strip().split()))
stack = []
result = []
for num in numbers[::-1]:
    while stack:
        if stack[-1] <= num:
            stack.pop()
        else:
            result.append(stack[-1])
            break
    if not stack:
        result.append(-1)
    
    stack.append(num)
    

print(*result[::-1])