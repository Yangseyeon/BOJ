import sys

def find_num(i, j):
    line = i + j - 1
    if line > n:
        i = n - i + 1
        j = n - j + 1
        if (i + j) % 2 == 0:
            return n**2 - ((i + j - 2) * (i + j - 1) // 2 + j ) + 1
        else:
            return n**2 - ((i + j - 2) * (i + j - 1) // 2 + i) + 1
    
    else:
        if (i + j) % 2 == 0:
            return (i + j - 2) * (i + j - 1) // 2 + j 
        else:
            return (i + j - 2) * (i + j - 1) // 2 + i


n, _ = map(int, sys.stdin.readline().strip().split())
func_string = sys.stdin.readline().strip()
result = 1
func_dict = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
i = 1
j = 1

for func in func_string:
    i, j = [i+ func_dict[func][0], j + func_dict[func][1]]

    result += find_num(i, j)

print(result)