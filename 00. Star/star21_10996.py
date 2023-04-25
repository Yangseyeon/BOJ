import sys
n = int(sys.stdin.readline().strip())

string1 = ""
string2 = ""
a = n
b = n -1
if n % 2==0:
    a = n - 1
    b = n


for j in range(a):
    if j % 2 == 0:
        string1 += "*"
    else:
        string1 += " "

for j in range(b):
    if j % 2 != 0:
        string2 += "*"
    else:
        string2 +=  " "


for i in range(2 * n):
    if i % 2== 0:
        print(string1)
    else:
        if n == 1:
            break
        print(string2)