import sys
sys.setrecursionlimit(10 ** 9)

def preorder(root):
    print(root, end = "")

    left = tree[root][0]
    right = tree[root][1]

    if left != ".":
        preorder(left)
    if right != ".":
        preorder(right)


def inorder(root):
    left = tree[root][0]
    right = tree[root][1]

    if left != ".":
        inorder(left)

    print(root, end = "")
    if right != ".":
        inorder(right)

def postorder(root):
    
    left = tree[root][0]
    right = tree[root][1]

    if left != ".":
        postorder(left)
    if right != ".":
        postorder(right)
    print(root, end = "")



tree = dict()
for _ in range(int(sys.stdin.readline().strip())):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]


preorder('A')
print()
inorder('A')
print()
postorder('A')
