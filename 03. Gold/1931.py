import sys
n = int(sys.stdin.readline().strip())
time_list = sorted(list(map(int, sys.stdin.readline().strip().split())) for _ in range(n))
time_list.sort(key = lambda x: x[1])

e = time_list[0][1]
cnt = 1

if n > 1:
    for start, end in time_list[1:]:
        if start >= e:
            e = end
            cnt += 1

print(cnt)