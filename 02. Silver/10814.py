import sys
n = int(sys.stdin.readline().strip())
member = list()

for i in range(n):
    age, name = sys.stdin.readline().strip().split()
    member.append([int(age), i, name])

member.sort()
for i in range(n):
    print(member[i][0], member[i][2])
