num = int(input())

num_list = []
for i in range(num):
    num_list.append(input())

num_list = list(set(num_list))
num_list.sort()
num_list.sort(key = len)
            
for string in num_list:
    print(string)