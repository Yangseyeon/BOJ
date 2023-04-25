import sys
n = int(sys.stdin.readline().strip())

star_list = [[' ' for j in range(5*(n//3) + (n//3 - 1))] for i in range(n)]

def print_star_recursive(tri_size, x, y):
    if tri_size == 3:
        for i in range(3):
            if i == 2:
                for j in range(3):
                    star_list[x + i][y - j] = "*"
                    star_list[x + i][y + j] = "*"
            else:
                star_list[x + i][y - i] = "*"
                star_list[x + i][y + i] = "*"
        return
    
    next_tri_size = tri_size // 2
    print_star_recursive(next_tri_size, x, y)
    print_star_recursive(next_tri_size, x + next_tri_size, y - next_tri_size)
    print_star_recursive(next_tri_size, x + next_tri_size, y + next_tri_size)

print_star_recursive(n, 0, n-1)
    
for row in star_list:
    print("".join(row))