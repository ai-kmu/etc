import numpy as np

input_info = input().split()
# 세로
N = int(input_info[0])
# 가로
M = int(input_info[1])


# map matrix
map = [[0 for _ in range(M)] for _ in range(N)]

# mark_map matrix
mark_map = [[0 for _ in range(M)] for _ in range(N)]


#map 정보 string
#map 받기
for i in range(0,N):
    map_info = input()
    for j in range(0,M):
        map[i][j] = int(map_info[j])

# 현재 있는 위치
current_p = np.array([0,0])

# queue
step_q = [current_p]
mark_map[0][0] = 1

# action space
right = np.array([0,1])
left = np.array([0,-1])
top = np.array([-1,0])
under = np.array([1,0])
dir_list = [under, right, left, top]

while step_q:
    current_p = step_q.pop(0)
    for dir in dir_list:
        next_p = dir + current_p
        if 0<=next_p[0] < N and 0<=next_p[1] < M :
            if map[next_p[0]][next_p[1]] == 1 and mark_map[next_p[0]][next_p[1]] <= 1:
                step_q.append(next_p)
                mark_map[next_p[0]][next_p[1]] = mark_map[current_p[0]][current_p[1]] +1


print(mark_map[N-1][M-1])





