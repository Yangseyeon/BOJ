num = int(input())

num_list = list(map(int, (input()).split(" ")))
cnt_all = 0
for n in num_list:
    flag = 1
    if n == 1:
        continue
    for i in range(2, n):
        if n % i == 0:
            flag = 0
            break
        if i * i >= n:
            break
            
    if flag == 1:
        cnt_all += 1
print(cnt_all)