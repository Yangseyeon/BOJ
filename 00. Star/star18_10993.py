import sys
n = int(sys.stdin.readline().strip())

star_pre_list = ["*"]
star_list = []

for cnt in range(n - 1):
    # print(star_pre_list)
    if cnt % 2 != 0:
        length = len(star_pre_list[-1])
    else:
        length = len(star_pre_list[0])

    end_length = length * 2 + 3
    height = len(star_pre_list) * 2 + 1
    
    if cnt % 2 != 0:
        for row in range(height):
            if row == 0:
                star_list.append(" " * (end_length//2 - row) + "*" + " " * (end_length//2 - row))
                continue

            if row == height - 1:
                star_list.append("*" * end_length)
                continue

            if row < len(star_pre_list):
                star_list.append(" " * (end_length//2 - row) + "*" + " " * (2 * row - 1) + "*" + " " * (end_length//2 - row))
            
            else:
                star_list.append(" " * (end_length//2 - row) + "*" +" " * (row - len(star_pre_list)) + star_pre_list[row - len(star_pre_list)] +" " * (row - len(star_pre_list)) + "*" + " " * (end_length//2 - row))
    
    else:
        for row in range(height):
            if row == height - 1:
                star_list.append(" " * (end_length//2) + "*" + " " * (end_length//2))
                continue

            if row == 0:
                star_list.append("*" * end_length)
                continue

            if row > len(star_pre_list):
                star_list.append(" " * row + "*" + " " * (length - 2 * (row - len(star_pre_list))) + "*" + " " * row)
            
            else:
                star_list.append(" " * row + "*" +" " * (len(star_pre_list) - row)+star_pre_list[row - 1] + " " * (len(star_pre_list) - row) + "*" + " " * row)
    
    star_pre_list = star_list
    star_list = []

for row in star_pre_list:
    print(row.rstrip())