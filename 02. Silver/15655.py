import sys
n, m = map(int, sys.stdin.readline().strip().split())
num_list = sorted(map(int,sys.stdin.readline().strip().split()))
permutation = [0 for i in range(m)]

def find_permutation(idx):
    if idx == m:
        print(*permutation)
        return
    start = 0
    if idx > 0:
        start = num_list.index(permutation[idx - 1]) + 1

    for i in range(start, len(num_list)):
        num = num_list[i]
        if num not in permutation:
            permutation[idx] = num
            find_permutation(idx + 1)
            permutation[idx] = 0
        

find_permutation(0)
    
