import sys
n = int(sys.stdin.readline().strip())
top = list(map(int, sys.stdin.readline().strip().split()))
stack = []

for i in range(n):
    while len(stack):
        if top[stack[-1]] < top[i]:
            stack.pop()

        else:
            print(stack[-1] + 1, end=" ")
            if top[stack[-1]] == top[i]:
                stack.pop()
                stack.append(i)
            break

    if len(stack) == 0:
        print(0, end=" ")
        stack.append(i)
    

    
