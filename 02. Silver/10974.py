n = int(input())
num_list = [0 for i in range(n)]

def find_permutation(idx):
    if idx == n:
        for num in num_list:
            print(num, end = " ")
        print()
        return
    for i in range(1, n+1):
        if i in num_list:
            continue
        num_list[idx] = i
        find_permutation(idx + 1)
        num_list[idx] = 0

find_permutation(0)