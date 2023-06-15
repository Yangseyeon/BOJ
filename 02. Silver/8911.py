import sys

for _ in range(int(sys.stdin.readline().strip())):
    string = sys.stdin.readline().strip()
    loc = [0, 0]
    d = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    idx = 0
    dot = [0, 0, 0, 0]
    
    for s in string:
        if s == "F":
            loc = [loc[0] + d[idx][0], loc[1] + d[idx][1]]
        elif s == "B":
            loc = [loc[0] - d[idx][0], loc[1] - d[idx][1]]
        elif s == "L":
            idx = idx + 1 if idx < 3 else 0
        elif s == "R":
            idx = idx - 1 if idx > 0 else 3

        dot = [max(dot[0], loc[0]), min(dot[1], loc[0]), max(dot[2], loc[1]), min(dot[3], loc[1])]

    print((dot[0] - dot[1])*(dot[2] - dot[3]))