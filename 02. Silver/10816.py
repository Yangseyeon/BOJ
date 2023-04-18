import sys

n = int(sys.stdin.readline().strip())
card_list = sorted(map(int, sys.stdin.readline().strip().split()))

m = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().strip().split()))
cnt_dict = dict()

def binary_search(num):
    start = 0
    end = n - 1

    while start <= end:
        
        mid = (start + end) // 2
        if card_list[mid] == num:
            return cnt_dict[num]
        elif card_list[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    
    return 0


for num in card_list:
    if num not in cnt_dict.keys():
        cnt_dict[num] = 1
    else:
        cnt_dict[num] += 1

for num in num_list:
    print(binary_search(num), end = " ")

