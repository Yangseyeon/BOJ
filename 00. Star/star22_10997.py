import sys
n = int(sys.stdin.readline().strip())

rec_pre = ["*****", "*    ", "* ***", "* * *", "* * *", "*   *", "*****"]
rec_new = []

for i in range(n - 2):
    pre_width = len(rec_pre[0])
    pre_height = len(rec_pre)
    width = pre_width + 4
    height = pre_height + 4

    for j in range(height):
        # print(rec_new)
        if j == 0 or j == height - 1:
            rec_new.append("*" * width)
            continue
        
        if j == 1:
            rec_new.append("*" + " " * (width - 1))
        
        elif j == 2:
            rec_new.append("* "+ rec_pre[j - 2] +"**")
        
        elif j == height - 2:
            rec_new.append("*" + " " * (width - 2) + "*")
            
        else:
            rec_new.append("* "+ rec_pre[j - 2] +" *")

    rec_pre = rec_new
    rec_new = []

if n == 1:
    print("*")
else:
    for row in range(len(rec_pre)):
        if row == 1:
            rec_pre[row] = "*"
        print(rec_pre[row])