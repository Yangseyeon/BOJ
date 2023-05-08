import sys
n = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().strip().split()))
count_list = list()

for i in range(n):
    cnt = 1
    for j in range(i):
        if num_list[j] < num_list[i] and count_list[j] >= cnt:
            cnt = count_list[j] + 1

    count_list.append(cnt)

print(count_list)
print(max(count_list))