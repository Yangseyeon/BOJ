import sys
n = int(sys.stdin.readline().strip())

f_a = dict()
stack = []
ngf = []
a = list(map(int, sys.stdin.readline().strip().split()))

for num in a:
    f_a[num] = 1 if num not in f_a.keys() else f_a[num] + 1

for num in a[::-1]:
    while stack:
        if f_a[stack[-1]] > f_a[num]:
            break
        stack.pop()
    
    if not stack:
        ngf.append(-1)
    else:
        ngf.append(stack[-1])
    stack.append(num)

print(*ngf[::-1])

        
