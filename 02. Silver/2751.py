import sys

n = int(sys.stdin.readline().strip())

num_list = list()
for i in range(n):
    num_list.append(int(sys.stdin.readline().strip()))

num_list.sort()

for num in num_list:
    print(num)