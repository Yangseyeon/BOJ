import sys
n = int(sys.stdin.readline().strip())
def print_star_recursive(size):
    if size == 1:
        return ["*"]
    

    next_size = size // 3
    pattern = print_star_recursive(next_size)

    star_list = []

    for p in pattern:
        star_list.append(p * 3)

    for p in pattern:
        star_list.append(p + next_size * " " + p)
    
    for p in pattern:
        star_list.append(p * 3)

    return star_list



star_list = print_star_recursive(n)

for row in star_list:
    
    print(row)