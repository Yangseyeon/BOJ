import sys

x_list = []
y_list = []

n = int(sys.stdin.readline().strip())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    x_list.append(x)
    y_list.append(y)


length = max((max(x_list) - min(x_list)), (max(y_list) - min(y_list)))


max_x = max(x_list)
min_x = min(x_list)
max_y = max(y_list)
min_y = min(y_list)


def find_case():

    # Case 1: 왼쪽 위 min_x, max_y
    # X-----
    # |    |
    # ------
    # print("Case 1", min_x, max_y)
    cnt = 0
    for i in range(n):
        x = x_list[i]
        y = y_list[i]

        if (x == min_x or x == min_x + length) and max_y  - length <= y <= max_y:
            cnt += 1
    
        elif (y == max_y or y == max_y - length) and min_x <= x <= min_x + length:
            cnt += 1

        else:
            break

    if cnt == n:
        return length
    
    # Case 2: 왼쪽 아래 min_x, min_y
    # ------
    # |    |
    # X-----
    # print("Case 2", min_x, min_y)
    cnt = 0
    for i in range(n):
        x = x_list[i]
        y = y_list[i]

        if (x == min_x or x == min_x + length) and min_y <= y <= min_y + length:
            cnt += 1
    
        elif (y == min_y or y == min_y + length) and min_x <= x <= min_x + length:
            cnt += 1

        else:
            break

    if cnt == n:
        return length
    

    # Case 3: 오른쪽 위 max_x, max_y
    # -----X
    # |    |
    # ------
    # print("Case 3", max_x, max_y)
    cnt = 0
    for i in range(n):
        x = x_list[i]
        y = y_list[i]

        if (x == max_x or x == max_x - length) and max_y - length <= y <= max_y:
            cnt += 1
    
        elif (y == max_y or y == max_y - length) and max_x - length <= x <= max_x:
            cnt += 1

        else:
            break

    if cnt == n:
        return length
    
    # Case 4: 왼쪽 아래 max_x, min_y
    # ------
    # |    |
    # -----X
    # print("Case 4", max_x, min_y)
    cnt = 0
    for i in range(n):
        x = x_list[i]
        y = y_list[i]

        if (x == max_x or x == max_x - length) and min_y <= y <= min_y + length:
            cnt += 1
    
        elif (y == min_y or y == min_y + length) and max_x - length <= x <= max_x:
            cnt += 1

        else:
            break

    if cnt == n:
        return length
    
    return -1


print(find_case())


