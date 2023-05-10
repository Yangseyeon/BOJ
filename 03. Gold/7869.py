import sys
import math
x1, y1, r, x2, y2, R = map(float, sys.stdin.readline().strip().split())

l = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if r + R <= l:
    result = 0

else:
    if l > abs(r - R):
        cos_theta1 = (R**2 + l**2 - r**2) / (2 * R * l)
        cos_theta2 = (r**2 + l**2 - R**2) / (2 * r * l)

        theta1 = math.acos(cos_theta1)
        theta2 = math.acos(cos_theta2)

        result = r**2 * theta2 + R ** 2 * theta1 - l * R * math.sin(theta1)

    else:
        if r > R:
            result = R ** 2 * math.pi
        
        else:
            result = r ** 2 * math.pi

print("%.3f" %result)