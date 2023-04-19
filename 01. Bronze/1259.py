import sys

while True:
    string = sys.stdin.readline().strip()
    if string == "0":
        break
    if string == string[::-1]:
        print("yes")
    else:
        print("no")