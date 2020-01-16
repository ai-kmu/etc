n = int(input())

lst_min = []
lst_max = []

for i in range(n):
    a,b = map(int,input().split())
    lst_min.append(a)
    lst_max.append(b)

counted = [False for i in range(min(lst_min),max(lst_max)+1,1)]

for i in range(n):
    for j in range(lst_min[i], lst_max[i], 1):
        counted[j] = True       
        
print(counted.count(1))
