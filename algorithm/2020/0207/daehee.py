from sys import stdin
import copy
#stdin.readline()

def dpe(number,ddp, cost, f):
# last dp
    this = dp(number-1,ddp,cost)
    
    ddp[number][f] = 10000001
    if f == 1:
        ddp[number][0] = min(this[1],this[2]) + cost[number][0]
        ddp[number][2] = min(this[1],this[0]) + cost[number][2]
    else:
        ddp[number][abs(f-1)] = min(this[f],this[abs(f-2)]) + cost[number][abs(f-1)]
        ddp[number][abs(f-2)] = min(this[f],this[abs(f-1)]) + cost[number][abs(f-2)]
    
    return min(ddp[number])


def dp(number,ddp, cost):
    if ddp[number][0] == 0:
        this = dp(number-1,ddp,cost)
        
        ddp[number][0] = min(this[1],this[2]) + cost[number][0]
        ddp[number][1] = min(this[0],this[2]) + cost[number][1]
        ddp[number][2] = min(this[0],this[1]) + cost[number][2]
        
    return ddp[number]



n = int(input())
# n = int(stdin.readline())


costs = [[0,0,0]]
for idx in range(n):
    costs.append(list(map(int,input().split(' '))))
    #costs.append(list(map(int,stdin.readline().split(' '))))
    
    

r = copy.deepcopy(costs)
r[1][1] = 1001
r[1][2] = 1001
g = copy.deepcopy(costs)
g[1][0] = 1001
g[1][2] = 1001
b = copy.deepcopy(costs)
b[1][1] = 1001
b[1][0] = 1001

rdp = [[0,0,0]] * 1001
gdp = [[0,0,0]] * 1001
bdp = [[0,0,0]] * 1001

rdp[1] = r[1]
gdp[1] = g[1]
bdp[1] = b[1]


print(min(dpe(n,rdp,r,0),dpe(n,gdp,g,1),dpe(n,bdp,b,2)))
