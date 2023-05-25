import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().strip().split())

result = 0

# 네 점이 한 직선 위에 있을 때 추가하기

if x2 != x1 and x4 != x3:
    m1 = (y2 - y1) / (x2 - x1)
    m2 = (y4 - y3) / (x4 - x3)
    if m1 - m2 != 0:
        x = (y3 - y1 + m1 * x1 - m2 * x3) / (m1 - m2)

        if min(x1, x2) <= x <= max(x1, x2) and min(x3, x4) <= x <= max(x3, x4):
            result = 1

    # 기울기 일치할 때
    else:
        # 두 직선이 서로 일치할 때
        if -m1 * x1 + y1 == -m2 *x3 + y3:
            if min(x1, x2) <= min(x3, x4) <=max(x1, x2) or min(x1, x2) <= max(x3, x4) <=max(x1, x2):
                result = 1
            
            elif min(x3, x4) <= min(x1, x2) <=max(x3, x4) or min(x3, x4) <= max(x1, x2) <=max(x3, x4):
                result = 1
        

else:
    if x1 == x2 and x3 == x4:
        if x1 == x3:
            if min(y1, y2) <= min(y3, y4) <= max(y1, y2) or min(y1, y2) <= max(y3, y4) <= max(y1, y2):
                result = 1
            elif min(y3, y4) <= min(y1, y2) <= max(y3, y4) or min(y3, y4) <= max(y1, y2) <= max(y3, y4):
                result = 1

    elif x3 == x4:
        m1 = (y2 - y1) / (x2 - x1)
        y = m1 * (x3 - x1) + y1

        if min(x1, x2) <= x3 <= max(x1, x2) and min(y3, y4) <= y <= max(y3, y4):
            result = 1

    elif x1 == x2:
        m2 = (y4 - y3) / (x4 - x3)
        y = m2 * (x1 - x3) + y3

        if min(x3, x4) <= x1 <= max(x3, x4) and min(y1, y2) <= y <= max(y1, y2):
            result = 1



print(result)