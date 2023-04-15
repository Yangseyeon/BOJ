num = int(input())

num_list = list(map(int, (input()).split(" ")))

num_list2 = num_list

num_list = list(set(num_list))
num_list.sort()

numdict = {}

for i in range(len(num_list)):
    numdict[num_list[i]] = i

for i in num_list2:
    print(numdict[i], end=' ')