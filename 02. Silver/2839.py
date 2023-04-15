num= int(input())

div = num // 5
flag = 0

for i in range(div, 0, -1):
    if  (num - i * 5) % 3 == 0:
        print(str(i + (num - i * 5) // 3))
        flag = 1
        break
        
if flag == 0:
    if num % 3 == 0:
        print(str(num // 3))
    
    else:
        print(str(-1))