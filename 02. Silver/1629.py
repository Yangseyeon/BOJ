import sys

a, b, c = map(int, sys.stdin.readline().strip().split())

# (a X b) % c == (a % c) * (b % c) % c

def mul(n):
    if n == 1:
        return a % c
    
    pre = mul(n//2)
    if n % 2 == 0:
        return (pre * pre) % c
    
    return(pre * pre * a) % c

print(mul(b))