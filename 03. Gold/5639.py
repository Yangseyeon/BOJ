import sys
sys.setrecursionlimit(10**9)

preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline().strip()))   
    except:
        break


def print_postorder(start, end):
    if start == end:
        print(preorder[start])
        return
    
    flag = 0
    for idx in range(start, end + 1):
        if preorder[idx] > preorder[start]:
            flag = 1
            break

    left_end = idx - 1
    
    if flag == 0:
        left_end = end

    if preorder[left_end] < preorder[start]:
        print_postorder(start + 1, left_end)
    
    if flag == 1:
        print_postorder(idx, end)

    print(preorder[start])


print_postorder(0, len(preorder) - 1)