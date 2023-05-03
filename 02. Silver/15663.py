import sys
n, m = map(int, sys.stdin.readline().strip().split())
num_list = sorted(map(int,sys.stdin.readline().strip().split()))
permutation = [-1 for i in range(m)]
visit_level = []

def find_permutation(idx):
    if idx == m:
        for i in permutation:
            print(num_list[i], end = " ")
        print()
        return
    
    
    check_num = 0
    for i in range(len(num_list)):
        if i in permutation or num_list[i] == check_num:
            continue

        check_num = num_list[i]
        permutation[idx] = i
        find_permutation(idx + 1)
        permutation[idx] = -1

find_permutation(0)