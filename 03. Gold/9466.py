import sys
sys.setrecursionlimit(10**9)

T = int(sys.stdin.readline().strip())
choice = []
visited = []
cycle = []
cnt = [0]

def dfs(idx):
    global cycle

    next_num = choice[idx]
    visited[idx] = 1
    cycle.append(idx)

    if visited[next_num] == 1:
        if next_num not in cycle:
            return
        while cycle:
            num = cycle.pop()
            cnt[0] += 1
            if num == next_num:
                break
        return
    
    
    dfs(next_num)

for _ in range(T):
    n = int(sys.stdin.readline().strip())
    cnt[0] = 0
    choice = [0] + list(map(int, sys.stdin.readline().strip().split()))
    visited = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if visited[i] == 1:
            continue
        cycle = []
        dfs(i)
    print(n - cnt[0])