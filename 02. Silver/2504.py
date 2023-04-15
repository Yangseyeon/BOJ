#2504
import sys

string = sys.stdin.readline().strip()
stack = list()
result = 0
tmp = 1
flag = 0

for index in range(len(string)):
    symbol = string[index]

    # print(symbol, result, tmp, index)
    if symbol == "(":
        tmp *= 2
        stack.append(symbol)
    
    elif symbol == "[":
        tmp *= 3
        stack.append(symbol)

    elif symbol == ")":
        if index == 0 or len(stack) == 0:
            flag = 1
            break

        if stack.pop() != "(":
            flag = 1
            break

        if string[index - 1] == "(":
            result += tmp
        tmp //= 2
    elif symbol == "]":
        if index == 0 or len(stack) == 0:
            flag = 1
            break

        if stack.pop() != "[":
            flag = 1
            break

        if string[index - 1] == "[":
            result += tmp
        tmp //= 3

if flag == 1 or len(stack) != 0:
    print(0)
else:
    print(result)