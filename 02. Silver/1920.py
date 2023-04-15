import sys

n = int(sys.stdin.readline().strip())
numbers1 = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
numbers2 = list(map(int, sys.stdin.readline().strip().split()))

numbers1.sort()

def is_in_numbers1(num):
    left_index = 0
    right_index = len(numbers1) - 1

    if num < numbers1[left_index] or num > numbers1[right_index]:
        return False

    while left_index <= right_index:
        
        mid = (left_index + right_index) // 2
        #print(left_index, mid, right_index)
        if numbers1[mid] == num:
            return True
        
        elif numbers1[mid] < num:
            left_index = mid + 1
        else:
            right_index = mid - 1
    
    return False

for num in numbers2:
    if is_in_numbers1(num):
        print(1)
    else:
        print(0)
    
    #print()
