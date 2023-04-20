import sys
t = int(sys.stdin.readline().strip())

for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().strip().split())
    room_h = n % h
    room_w = n//h + 1
    
    if n % h == 0:
        room_h = h
        room_w -= 1

    print(room_h* 100 + room_w)