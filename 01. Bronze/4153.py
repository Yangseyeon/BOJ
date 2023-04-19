import sys

while True:
    numbers = sorted(map(int, sys.stdin.readline().strip().split()))
    if numbers[0] == 0:
        break

    if numbers[2] ** 2 == numbers[0] ** 2 + numbers[1] ** 2:
        print("right")
    else:
        print("wrong")
