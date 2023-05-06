import sys
n = int(sys.stdin.readline().strip())
num_list = [0 for _ in range(n)]

for i in range(n):
    l = list(map(int, sys.stdin.readline().strip().split()))
    tmp1 = num_list[0]

    for j in range(len(l)):
        tmp2 = num_list[j]

        if j == 0:
            num_list[j] += l[j]
            continue

        elif j == len(l) - 1:
            num_list[j] = tmp1 + l[j]
            continue
        
        num_list[j] = max(tmp1, num_list[j]) +l[j]
        tmp1 = tmp2

print(max(num_list))