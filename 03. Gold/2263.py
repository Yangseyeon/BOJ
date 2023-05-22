import sys

n = int(sys.stdin.readline().strip())

inorder = list(map(int, sys.stdin.readline().strip().split()))
postorder = list(map(int, sys.stdin.readline().strip().split()))

p = [0 for _ in range(n + 1)]
for i in range(n):
    p[inorder[i]] = i


def find_preorder(i_start, i_end, p_start, p_end):
    if i_start > i_end or p_start > p_end:
        return

    root_node = postorder[p_end]
    print(root_node, end = " ")

    left = p[root_node] - i_start
    right = i_end - p[root_node]

    find_preorder(i_start, i_start + left - 1, p_start, p_start + left - 1)
    find_preorder(i_end - right + 1, i_end, p_end - right, p_end - 1)
            

find_preorder(0, n - 1, 0, n - 1)