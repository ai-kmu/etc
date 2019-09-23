mtx = [] 
n,m = map(int,input().strip().split())

for j in range(n):
    mtx.append([])
    for i in input():
        if i =='0':
            mtx[j].append(0) 
        else:
            mtx[j].append(1) 
        
col = [-1,0,1,0]
row = [0,1,0,-1]
end = [n-1,m-1]

def solution(mtx):
    position = [[0,0]]
    c = 0 
    r = 0
    while c != n-1 or r != m-1:
        c = position[-1][0]
        r = position[-1][1]
        v = mtx[c][r]
        for i in range(4):
            t_col  = c + col[i]
            t_row = r + row[i]
            if t_col < 0 or t_row <0 or t_col >= n or t_row >= m:
                continue
            tv = mtx[t_col][t_row]
            if tv < 1 :
                continue 
            if tv == 1 or v + 1 < tv :
                mtx[t_col][t_row] = v + 1
                position.append([t_col,t_row])
    return mtx[end[0]][end[1]]
    

print(solution(mtx))
