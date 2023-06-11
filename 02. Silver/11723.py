import sys

s = set()

for _ in range(int(sys.stdin.readline().strip())):
    func = list(sys.stdin.readline().strip().split())
    
    if func[0] == "add":
        s.add(func[1])
    elif func[0] == "remove":
        s.discard(func[1])
    elif func[0] == "check":
        print(1 if func[1] in s else 0)
    elif func[0] == "toggle":
        s.discard(func[1]) if func[1] in s else s.add(func[1])
    elif func[0] == "all":
        s = set([str(i) for i in range(1, 21)])
    elif func[0] == "empty":
        s = set()