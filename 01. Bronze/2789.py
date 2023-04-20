import sys
n, m = map(int, sys.stdin.readline().strip().split())
card_list = sorted(map(int, sys.stdin.readline().strip().split()))[::-1]
max_sum = 0

for i in range(len(card_list) - 2):
    if card_list[i]>= m:
            continue
    for j in range(i+1, len(card_list) -1):
        if card_list[i] + card_list[j] >= m:
            continue
        for k in range(j+1, len(card_list)):
            s = card_list[i]+ card_list[j]+ card_list[k]
            if max_sum < s <= m:
                max_sum = s
            if max_sum == m:
                break

print(max_sum)
