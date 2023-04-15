import sys
        
n, m = map(int, sys.stdin.readline().strip().split())

def is_prime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

        if i >= num / i:
            break
        
    return True

for i in range(n, m+1):
    if is_prime(i):
        print(i)