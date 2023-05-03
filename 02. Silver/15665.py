import sys
n, m = map(int, sys.stdin.readline().strip().split())
num_list = sorted(set(map(int,sys.stdin.readline().strip().split())))
permutation = [-1 for i in range(m)]
visit_level = []

def find_permutation(idx):
    if idx == m:
        for i in permutation:
            print(num_list[i], end = " ")
        print()
        return

    for i in range(len(num_list)):
        permutation[idx] = i
        find_permutation(idx + 1)

find_permutation(0)