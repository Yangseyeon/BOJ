import sys
n = int(sys.stdin.readline().strip())

string1 = ""
string2 = ""

for j in range(2 * n - 1):
    if j % 2 == 0:
        string1 += "*"
    else:
        string1 += " "

for j in range(2 * n):
    if j % 2 != 0:
        string2 += "*"
    else:
        string2 += " "
        

for i in range(n):
    if i % 2== 0:
        print(string1)
    else:
        print(string2)