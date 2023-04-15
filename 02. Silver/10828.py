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
        
n = int(sys.stdin.readline())
stack = Stack()
for i in range(n):
    func = sys.stdin.readline().strip().split()
    if func[0] == "push":
        stack.push(int(func[1]))
    elif func[0] == "pop":
        print(stack.pop())
    elif func[0] == "size":
        print(stack.size())
    elif func[0] == "empty":
        if stack.isEmpty():
            print(1)
        else:
            print(0)
    elif func[0] == "top":
        print(stack.top())