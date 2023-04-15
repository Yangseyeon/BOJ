#Stack 구현
n = int(input())
math_exp = input()
numbers = list()

class Stack:
    def __init__(self):
        self.stack = list()
    
    def push(self, elem):
        self.stack.append(elem)
    
    def pop(self):
        if bool(len(self.stack)) == False:
            return
        return self.stack.pop()
    def isEmpty(self):
        return len(self.stack) == 0 
    def size(self):
        return len(self.stack)
    def top(self):
        if bool(len(self.stack)) == False:
            return
        return self.stack[-1]
    def traverse(self):
        for i in self.stack:
            print(i, end = " ")
        print()

        
#수식 평가
        
def is_number(elem):
    if ord("A") <= ord(elem) <= ord("Z"):
        return True
    else:
        return False

def cal(num1, num2, symbol):
    if symbol == '+':
        return num1 + num2
    elif symbol == '-':
        return num1 - num2
    elif symbol == '*':
        return num1 * num2
    else:
        return num1 / num2
    
def convert_num(elem):
    return numbers[ord(elem) - ord("A")]

for i in range(n):
    numbers.append(int(input()))

stack_eva = Stack()

for elem in math_exp:
    if is_number(elem):
        stack_eva.push(convert_num(elem))
    else:
        num1 = float(stack_eva.pop())
        num2 = float(stack_eva.pop())
        stack_eva.push(cal(num2, num1, elem))

print("%.2f" %stack_eva.pop())