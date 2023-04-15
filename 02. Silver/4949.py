#4949
import sys

def is_balance_str(string):
    stack = list()
    for symbol in string:
        if symbol == "(" or symbol == "[":
            stack.append(symbol)
        
        elif symbol == ")":
            if len(stack) == 0:
                return False
            if stack.pop() != "(":
                return False
        elif symbol == "]":
            if len(stack) == 0:
                return False
            if stack.pop() != "[":
                return False
    
    if len(stack) != 0:
        return False
    else:
        return True
        

while True:
    string = sys.stdin.readline().rstrip()

    if string == ".":
        break
    if is_balance_str(string):
        print("yes")
    else:
        print("no")
    
