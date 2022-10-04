def solution(triangle):
    answer = 0
    tri_len = len(triangle)
    
    # tri[1][0] = tri[0][0] + tri[1][0]
    # tri[1][1] = tri[0][0] + tri[1][1]
    # tri[2][0] = tri[1][0] + tri[2][0]
    # tri[2][2] = tri[1][1] + tri[2][2]
    # tri[3][0] = tri[2][0] + tri[3][0]
    # tri[3][3] = tri[2][2] + tir[3][3]
    # ...
    # tri[2][1] = max(tri[1][0] + tri[2][1], tri[1][1] + tri[2][1])
    # tri[3][2] = max(tri[2][1] + tri[3][2], tri[2][2] + tri[3][2])
    # 외곽 먼저 다 더해주고, 나머지 max
    triangle[1][0] = triangle[0][0] + triangle[1][0]
    triangle[1][1] = triangle[0][0] + triangle[1][1]
    
    for n in range(2, tri_len):
        triangle[n][0] = triangle[n-1][0] + triangle[n][0]
        triangle[n][n] = triangle[n-1][n-1] + triangle[n][n]
    
    for k in range(2, tri_len):
        for j in range(1, len(triangle[k-1])): # 3,4,5
            #print(triangle[k][j])
            
            triangle[k][j] = max(triangle[k-1][j-1] + triangle[k][j], triangle[k-1][j] + triangle[k][j])
    answer = max(triangle[tri_len - 1])
    
        
    return answer
