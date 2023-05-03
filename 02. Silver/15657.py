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
        start = num_list.index(permutation[idx - 1])
    
    for i in range(start, len(num_list)):
        permutation[idx] = num_list[i]
        find_permutation(idx + 1)
    


find_permutation(0)