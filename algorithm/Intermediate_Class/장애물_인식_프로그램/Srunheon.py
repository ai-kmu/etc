import sys

map_size = int(input())
zido = []
for i in range(map_size):
    b = input()
    zido.append(list(map(int,list(b))))

# 상 하 좌 우
# y, x 
direction = [(-1,0), (1,0), (0,-1), (0,1)]

# 현재 위치에서 탐색해서 모두 도달할때까지 이동
def explore(cur_i, cur_j, block_n = 0):

    # 방문처리
    zido[cur_i][cur_j] = 0

    # 4 방향으로 이동
    # 범위밖은 이동하지 않음
    # 방문했으면 이동하지 않음
    for to_i, to_j in direction:
        if cur_i + to_i < 0 or cur_i + to_i >= map_size:
            continue
        if cur_j + to_j < 0 or cur_j + to_j >= map_size:
            continue 
        if zido[cur_i + to_i ][cur_j + to_j] == 0:
            continue 
        block_n += explore(cur_i + to_i, cur_j + to_j, 0)
    return block_n + 1

count = 0
answer = []
for i in range(map_size):
    for j in range(map_size):
        if zido[i][j] == 0:
            continue
        else:
            count += 1
            answer.append(explore(i, j, 0))

print(count)
answer.sort()
for i in answer:
    print(i)
