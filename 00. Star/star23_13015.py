import sys
n = int(sys.stdin.readline().strip())

for i in range(n):
    for j in range(2 * n - 1):
        if i == 0 and j < n:
            sys.stdout.write("*")
            continue

        if j == i or j == n + i -1:
            sys.stdout.write("*")
        else:
            sys.stdout.write(" ")
    for j in range(2 * n - 3, -1, -1):
        if i == 0 and j < n:
            sys.stdout.write("*")
            continue

        if j == i or j == n + i -1:
            sys.stdout.write("*")
        else:
            sys.stdout.write(" ")
        if j == i:
            break
    sys.stdout.write("\n")

for i in range(n-2, -1, -1):
    for j in range(2 * n - 1):
        if i == 0 and j < n:
            sys.stdout.write("*")
            continue

        if j == i or j == n + i -1:
            sys.stdout.write("*")
        else:
            sys.stdout.write(" ")
    for j in range(2 * n - 3, -1, -1):
        if i == 0 and j < n:
            sys.stdout.write("*")
            continue

        if j == i or j == n + i -1:
            sys.stdout.write("*")
        else:
            sys.stdout.write(" ")
        if j == i:
            break
    sys.stdout.write("\n")