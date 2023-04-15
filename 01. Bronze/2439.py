num_list = list()

def print_num(num1, num2):
    for num in num_list:
        if num == num1 or num == num2:
            continue
        print(num)

for i in range(9):
    num = int(input())
    num_list.append(num)

flag = 0
for idx1 in range(9):
    num1 = num_list[idx1]
    for idx2 in range(idx1 + 1, 9):
        num2 = num_list[idx2]
        if sum(num_list) - (num1 + num2) == 100:
            flag = 1
            print_num(num1, num2)
            break
    if flag == 1:
        break