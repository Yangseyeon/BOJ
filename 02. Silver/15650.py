n, m = map(int, (input()).split(" "))
num_list = [0 for i in range(m)]

def find_permutation(idx):
    if idx == m:
        for num in num_list:
            print(num, end = " ")
        print()
        return
    start = 1
    if idx != 0:
        start = num_list[idx - 1] + 1
    for i in range(start, n+1):
        num_list[idx] = i
        find_permutation(idx + 1)
        num_list[idx] = 0

find_permutation(0)