import sys
n = int(sys.stdin.readline().strip())
pay = [0] * (n + 1)
max_pay = 0

for i in range(n):
    max_pay = max(max_pay, pay[i])
    t, p = map(int, sys.stdin.readline().strip().split())
    if i + t > n:
        continue
    pay[i + t] = max(max_pay + p, pay[i + t])
    
print(max(max_pay, pay[n]))