import sys

n, m = map(int, sys.stdin.readline().strip().split())

num_a = n
num_b = m

if n < m:
    num_a = m
    num_b = n

while True:
    mod = num_a % num_b
    if mod == 0:
        break
    num_a = num_b
    num_b = mod

print(num_b)
print(n*m // num_b)

