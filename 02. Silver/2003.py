import sys
n, m = map(int, sys.stdin.readline().strip().split())
numbers = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0

sum = numbers[0]
left = 0
right = 1
cnt = 0

while True:
    if sum < m:
        if right < n:
            sum += numbers[right]
            right += 1
        else:
            break
    elif sum == m:
        cnt += 1
        sum -= numbers[left]
        left += 1
    else:
        sum -= numbers[left]
        left += 1

print(cnt)
