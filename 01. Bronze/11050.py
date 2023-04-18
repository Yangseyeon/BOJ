import sys
n, k = map(int, sys.stdin.readline().strip().split())
coef = 1
fac = 1

if k > n // 2:
    k = n - k


for i in range(k):
    coef *= (n - i)
    fac *= (k - i)

print(coef // fac)



