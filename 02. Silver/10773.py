import sys

n = int(sys.stdin.readline().strip())

num_list = list()
for i in range(n):
    num = int(sys.stdin.readline().strip())

    if num == 0:
        num_list.pop()

    else:
        num_list.append(num)

print(sum(num_list))