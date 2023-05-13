import sys

n = int(sys.stdin.readline().strip())

def move_top(n, start, end):
    if n == 1:
        print(start, end)
        return
    
    index = [start, 1]
    if 2 not in [start, end]:
        index[1] = 2
    elif 3 not in [start, end]:
        index[1] = 3
    flag = 0

    for i in range(n-1, 0, -1):
        move_top(i, index[flag], index[1 - flag])
        print(index[flag], end)
        
        flag = 1- flag
    print(index[flag], end)
    
    
print(2**n - 1)
move_top(n, 1, 3)
