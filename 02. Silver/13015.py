import sys
n = int(sys.stdin.readline().strip())

for i in range(n):
    for j in range(2 * n - 1):
        if i == 0 and j < n:
            print("*", end = "")
            continue

        if j == i or j == n + i -1:
            print("*", end = "")
        else:
            print(" ", end = "")
    for j in range(2 * n - 3, -1, -1):
        if i == 0 and j < n:
            print("*", end = "")
            continue

        if j == i or j == n + i -1:
            print("*", end = "")
        else:
            print(" ", end = "")
        if j == i:
            break
    print()

for i in range(n-2, -1, -1):
    for j in range(2 * n - 1):
        if i == 0 and j < n:
            print("*", end = "")
            continue

        if j == i or j == n + i -1:
            print("*", end = "")
        else:
            print(" ", end = "")
    for j in range(2 * n - 3, -1, -1):
        if i == 0 and j < n:
            print("*", end = "")
            continue

        if j == i or j == n + i -1:
            print("*", end = "")
        else:
            print(" ", end = "")
        if j == i:
            break
    print()