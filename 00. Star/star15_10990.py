import sys
n = int(sys.stdin.readline().strip())

for i in range(n):
    if i == 0:
        print(" " * (n - i - 1) + "*")
        continue
    print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")