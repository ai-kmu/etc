
def solution(maps):

    map_row_size = len(maps)
    map_col_size = len(maps[0])

    queue = list()
    dist = 0
    is_arrived = False

    #(0,0)에서 게임 시작 !
    # (row,col,dist)
    queue.append((0,0,1))

    while(len(queue)) :

        current_row = queue[0][0]
        current_col = queue[0][1]
        dist = queue[0][2]
        del queue[0]

        # 상대팀 진영에 도착하면 끝!
        if current_row == map_row_size-1 and current_col == map_col_size-1:
            is_arrived = True
            break

        # 위로 갈 수 있는 경우
        if current_row-1 >= 0 and maps[current_row-1][current_col] == 1 :
            queue.append((current_row-1, current_col, dist+1))
            # 간 경로는 더이상 못가도록 0으로 바꿔준다.
            maps[current_row-1][current_col] = 0

        # 아래로 갈 수 있는 경우
        if current_row+1 <= map_row_size-1 and maps[current_row+1][current_col] == 1 :
            queue.append((current_row+1, current_col, dist+1))
            maps[current_row + 1][current_col] = 0

        # 왼쪽으로 갈 수 있는 경우
        if current_col-1 >= 0 and maps[current_row][current_col-1] == 1 :
            queue.append((current_row, current_col-1, dist+1))
            maps[current_row][current_col - 1] = 0

        # 오른쪽으로 갈 수 있는 경우
        if current_col+1 <= map_col_size-1  and maps[current_row][current_col+1] == 1 :
            queue.append((current_row, current_col+1, dist+1))
            maps[current_row][current_col + 1] = 0

    # 갈 수 있는 곳이 없어서 while문이 끝났는데 상대방진영이 아니라면 -1 
    if is_arrived != True:
        return -1
    return dist
