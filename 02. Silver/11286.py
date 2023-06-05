from heapq import heappush, heappop
import sys
heap = []

for _ in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            num = heappop(heap)
            print(num[-1])
        continue

    heappush(heap, [abs(n), n])