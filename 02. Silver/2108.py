import sys

n = int(sys.stdin.readline().strip())
num_list = list()
num_dict = dict()

for i in range(n):
    num = int(sys.stdin.readline().strip())
    num_list.append(num)

    if num not in num_dict.keys():
        num_dict[num] = 0
    else:
        num_dict[num] += 1

num_list.sort()
sum_numbers = sum(num_list)

print(round(sum_numbers / n))
print(num_list[n//2])

mode_max = max(num_dict.values())
mode_list = list()

for key in num_dict.keys():
    if num_dict[key] == mode_max:
        mode_list.append(key)

mode_list.sort()
if len(mode_list) != 1:
    print(mode_list[1])
else:
    print(mode_list[0])

print(max(num_list) - min(num_list))

    
