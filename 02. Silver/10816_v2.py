import sys

n = int(sys.stdin.readline().strip())
card_list = list(map(int, sys.stdin.readline().strip().split()))

m = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().strip().split()))

cnt_dict = dict()

for num in card_list:
    if num not in cnt_dict.keys():
        cnt_dict[num] = 1
    else:
        cnt_dict[num] += 1

for num in num_list:
    if num in cnt_dict.keys():
        print(cnt_dict[num], end=" ")
    else:
        print(0, end = " ")
