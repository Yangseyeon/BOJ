import sys
n, m = map(int, sys.stdin.readline().strip().split())
num = [0] + list(map(int, sys.stdin.readline().strip().split()))

for i in range(n + 1):
    num[i] += num[i - 1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(num[j] - num[i - 1])