import sys
n = int(sys.stdin.readline().strip())

for i in range(1, n + 1):
    if i == n:
        print("*" * (2 * i - 1))
        continue
    string = " " * (n - i)
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            string += "*"
        else:
            string += " "

    print(string)