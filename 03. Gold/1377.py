import sys

n = int(sys.stdin.readline().strip())
num_list = list()

for i in range(n):
    num_list.append([int(sys.stdin.readline().strip()), i])

sort_list = sorted(num_list)

flag = 0
max_gap = 0

for i in range(n):
    gap = sort_list[i][1] - num_list[i][1]
    if flag == 0:
        flag = 1
        max_gap = gap
        continue

    if max_gap < gap:
        max_gap = gap

print(max_gap + 1)


