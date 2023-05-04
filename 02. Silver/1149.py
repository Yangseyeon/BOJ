import sys
n = int(sys.stdin.readline().strip())
RGB = []

for i in range(n):
    r, g, b = map(int, sys.stdin.readline().strip().split())
    
    if i == 0:
        RGB = [r, g, b]
        continue

    RGB = [min(RGB[1], RGB[2]) + r, 
           min(RGB[0], RGB[2]) + g,
           min(RGB[0], RGB[1]) + b]
    
print(min(RGB))

