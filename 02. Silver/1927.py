from heapq import heappush, heappop
import sys
heap = []

for _ in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap))
        continue

    heappush(heap, n)