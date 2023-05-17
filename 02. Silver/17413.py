import sys
string = sys.stdin.readline().strip()

str_stack = []
result = ""
i = 0

while i < len(string):
    if string[i] == " ":
        while str_stack:
            result += str_stack.pop()
        result += " "

        i += 1
    
    elif string[i] == "<":
        while str_stack:
            result += str_stack.pop()
        
        while string[i] != ">":
            result += string[i]
            i += 1

        result += string[i]
        i += 1

    else:
        str_stack.append(string[i])

        i += 1

while str_stack:
    result += str_stack.pop()

print(result)
    

    

