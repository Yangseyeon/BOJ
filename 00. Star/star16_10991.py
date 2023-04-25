import sys
n = int(sys.stdin.readline().strip())

for i in range(1, n + 1):
    string = " " * (n - i)
    for j in range(2 * i - 1):
        if j % 2== 0:
            string += "*"
        else:
            string += " "

    print(string)