import sys

class Stack:
    def __init__(self):
        self.stack = list()
    
    def push(self, elem):
        self.stack.append(elem)
    
    def pop(self):
        if bool(len(self.stack)) == False:
            return -1
        return self.stack.pop()
    def isEmpty(self):
        return len(self.stack) == 0 
    def size(self):
        return len(self.stack)
    def top(self):
        if bool(len(self.stack)) == False:
            return -1
        return self.stack[-1]
    def traverse(self):
        for i in self.stack:
            print(i, end = " ")
        print()


def is_vps(PS):
    stack = Stack()
    for symbol in PS:
        if symbol == "(":
            stack.push(symbol)
        elif symbol == ")":
            if stack.isEmpty():
                return False
            else:
                stack.pop()
    
    if stack.isEmpty():
        return True
    else:
        return False
    
n = int(sys.stdin.readline().strip())
for i in range(n):
    string = sys.stdin.readline().strip()
    if is_vps(string):
        print("YES")
    else:
        print("NO")