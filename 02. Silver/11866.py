import sys

n, k = map(int, sys.stdin.readline().strip().split())
num_list = [i for i in range(1, n + 1)]

string = "<"
flag = 0
index = k
while len(num_list):
    
    index = (index - 1)%len(num_list)
    if flag == 0:
        flag = 1
    else:
        string += ", "
    string += str(num_list[index])
    del num_list[index]
    index = index +k
print(string+">")