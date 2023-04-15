import sys

n, meter = map(int, sys.stdin.readline().strip().split())
tree_list = list(map(int, sys.stdin.readline().strip().split()))

tree_list.sort()
tree_list.reverse()

def binary_search(meter):
    min_height = 1
    max_height = tree_list[0]

    mid = 0
    while min_height <= max_height:
        
        mid = (min_height + max_height) // 2
        cut_height = 0
        for tree in tree_list:
            if tree < mid:
                break
            cut_height += (tree - mid)
        if cut_height > meter:
            min_height = mid + 1
        elif cut_height == meter:
            return mid
        else:
            max_height = mid - 1
    
    return max_height
print(binary_search(meter))