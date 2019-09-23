goal_x,goal_y=map(int,input().split())#리눅스 스탠다드 input으로 받는다.
maze = [list(map(int, list(input()))) for i in range(goal_x)]#미로를 리스트 형태로 바꾼다.
goal=[goal_x-1,goal_y-1]
move=[[0,1],[-1,0],[1,0],[-1,0]]#상,하,좌,우
visit=[[0]*goal_y for i in range(goal_x)]#방문 했는지 점검
dist=[[0]*goal_y for i in range(goal_x)]#이동거리 계산
pos=[]#좌
dist[0][0]=1
visit[0][0]=1
pos.append((0,0))

while pos:
    x,y=pos.pop(0)
    for i in range(4):
        move_x=x+move[i][0]
        move_y=y+move[i][1]
        if (move_x<0 and move_x>=goal_x) or (move_y<0 and move_y>=goal_y): #이동한게 벽이면 다시 탐색
            continue
        if 0<=move_x<goal_x and 0<=move_y<goal_y and visit[move_x][move_y]==0 and maze[move_x][move_y]==1:#이동한 곳이 미로 안에 있고 방문한 적이 없고 미로가 갈수 있는 곳이면 탐색
                pos.append((move_x,move_y))
                dist[move_x][move_y]=dist[x][y]+1
                visit[move_x][move_y]=1

print(dist[goal_x-1][goal_y-1])
