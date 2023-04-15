n, m = map(int, (input()).split(" "))
num_list = [0 for i in range(m)]

def find_permutation(idx):
    if idx == m:
        for num in num_list:
            print(num, end = " ")
        print()
        return
    for i in range(1, n+1):
        num_list[idx] = i
        find_permutation(idx + 1)
        num_list[idx] = 0

find_permutation(0)