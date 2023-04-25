import sys
n = int(sys.stdin.readline().strip())

rec_pre = ["*"]
rec_new = []

for i in range(n - 1):
    pre_width = len(rec_pre[0])
    width = pre_width + 4

    for j in range(width):
        # print(rec_new)
        if j == 0 or j == width - 1:
            rec_new.append("*" * width)
            continue
        
        if j == 1 or j == width - 2:
            rec_new.append("*" + " " * (width - 2) + "*")
            
        else:
            rec_new.append("* "+ rec_pre[j - 2] +" *")

    rec_pre = rec_new
    rec_new = []

for row in rec_pre:
    print(row)