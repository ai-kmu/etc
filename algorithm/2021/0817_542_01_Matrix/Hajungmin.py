if mat == None or len(mat) == 0:
    return mat

q = deque()
rows = len(mat)
cols = len(mat[

# 만약 현재 셀이 0이면 큐에 넣고 아니면 -1을
for i in range(rows):
    for j in range(cols):
        if mat[i][j] == 0:
            q.append((i,j))
        else:
            mat[i][j] = -1
# 거리는 1로 만들어준다
dist = 1
#이후 현재 위치에서부터 BFS를 해준다
while q:
    for i in range(len(q)):
        currpos = q.popleft()
        directions = [(-1, 0), (0, 1), (1, 0), (0,-1)]
        # 위, 오른쪽, 아래, 왼쪽 순으로 검사한다
        for direction in directions:
            next_row = currpos[0] + direction[0]
            next_col = currpos[1] + direction[1]
            #다음 row와 col이 0보다 크거나 같고 최대 row와 col의 길이보다 작고 현재 -1일 경우 큐에 다음 row와 col을 더해주고 현재 거리값을 넣어준다
            if next_row>= 0 and next_col >= 0 and next_row < len(mat) and next_col < len(mat[0]) and mat[next_row][next_col] == -1:
                q.append((next_row,next_col))
                mat[next_row][next_col] = dist
						
    # 거리를 1더해준다
    dist += 1

return mat
