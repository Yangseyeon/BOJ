import sys
n, m = map(int, sys.stdin.readline().strip().split())
num_list = sorted(map(int,sys.stdin.readline().strip().split()))
permutation = [0 for i in range(m)]

def find_permutation(idx):
    if idx == m:
        print(*permutation)
        return
    
    for num in num_list:
        permutation[idx] = num
        find_permutation(idx + 1)
        

find_permutation(0)
    
