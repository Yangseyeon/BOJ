#Stack 구현

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
        
# 후위수식으로 전환

math_exp = input()
convert_list = list()
stack = Stack()

def symbol_rank(symbol):
    if symbol == "+" or symbol == "-":
        return 1
    elif symbol == "*" or symbol == "/":
        return 2
    elif symbol == "(" or symbol == ")":
        return 0
    else:
        return -1
    
def is_number(elem):
    if elem != "+" and elem != "-" and elem != "*" and elem != "/" and elem != "(" and elem != ")":
        return True
    else:
        return False
    
for elem in math_exp:
    if is_number(elem):
        convert_list.append(elem)
    else:
        if stack.isEmpty():
            stack.push(elem)
        
        elif elem == "(":
            stack.push(elem)
            
        elif elem == ")":
            while stack.isEmpty() == False:
                if stack.top() == "(":
                    break
                convert_list.append(stack.pop())
            stack.pop()

        else:
            while stack.isEmpty() == False:
                if symbol_rank(stack.top()) >= symbol_rank(elem):
                    convert_list.append(stack.pop())
                else:
                    break
            stack.push(elem)
                
while stack.isEmpty() == False:
    convert_list.append(stack.pop())

for i in convert_list:
    print(i, end = "")
