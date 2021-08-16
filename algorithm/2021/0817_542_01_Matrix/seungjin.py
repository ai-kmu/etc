def updateMatrix(mat):
    m ,n = len(mat) , len(mat[0])
    dir = [0, 1, 0, -1, 0]
    q = []
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                q.append((i,j))
            else:
                mat[i][j] = -1

    while q:
        a ,b = q.pop(0)
        for i in range(4):
            next_a , next_b = a+dir[i] , b+dir[i+1]
            if next_a < 0 or next_a == m or next_b < 0 or next_b == n or mat[next_a][next_b] != -1: continue
            mat[next_a][next_b] = mat[a][b] +1
            q.append((next_a , next_b))
    return mat
