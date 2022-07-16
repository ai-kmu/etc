import sys
from collections import deque

n = int(sys.stdin.readline())
Map = [list(sys.stdin.readline().strip()) for i in range(n)]

def bfs(start_point):
    count = 0
    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    Map_queue = deque()

    Map_queue.append(start_point)
    count += 1

    while Map_queue:
        r, c = Map_queue.popleft()
        for y,x in direction:
            new_r = r + y
            new_c = c + x
            if 0 <= new_r < n and 0 <= new_c < n:
                if Map[new_r][new_c] == '1':
                    Map[new_r][new_c] = '0'
                    Map_queue.append([new_r,new_c])
                    count += 1
    return count

ob_num_list = []


for i in range(n):
    for j in range(n):
        if Map[i][j] == '1':
            Map[i][j] = '0'
            start_point = [i,j]
            count = bfs(start_point)
            ob_num_list.append(count)

answer_list = sorted(ob_num_list)

print(len(answer_list))
for i in range(len(answer_list)):
    print(answer_list[i])
