import sys
n , m= map(int, sys.stdin.readline().strip().split())

if m > n //2:
    m = n - m

num = 1
div = 1

for i in range(1, m + 1):
    num *= (n - i + 1)
    div *= i

print(num //div)