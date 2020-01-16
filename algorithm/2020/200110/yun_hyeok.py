N = int(input())

min_list = []
max_list = []

for _ in range(N):
    a,b = map(int, input().split())
    min_list.append(a)
    max_list.append(b)

counted = [False for _ in range(min(min_list), max(max_list) + 1, 1)]

for i in range(N):
    for j in range(min_list[i], max_list[i], 1):
        counted[j] = True       
        
print(counted.count(1))
