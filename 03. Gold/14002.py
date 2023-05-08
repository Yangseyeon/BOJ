import sys
n = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().strip().split()))
count_list = list()
route = list()

for i in range(n):
    cnt = 1
    idx = i
    for j in range(i):
        if num_list[j] < num_list[i] and count_list[j] >= cnt:
            cnt = count_list[j] + 1
            idx = j

    route.append(idx)
    count_list.append(cnt)


print_route = []

idx = count_list.index(max(count_list))
while count_list[idx] != 1:
    print_route.append(num_list[idx])
    idx = route[idx]

print_route.append(num_list[idx])
print_route.reverse()
print(*print_route)

print(max(count_list))