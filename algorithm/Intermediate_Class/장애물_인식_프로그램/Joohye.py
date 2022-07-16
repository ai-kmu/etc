# C++ 코드 참고 풀이
import sys
# 받아오는 코드
input = sys.stdin.readline
s = int(input())
graph = []
temp = []
result = 0
summ = 0
for i in range(s):
    graph.append(list(map(int,input().rstrip())))

def dfs(x,y):
    global summ
    # 주어진 범위를 벗어나지않도록
    if x <= -1 or x >= s or y <= -1 or y >= s:
        return False
    # 아직 방문하지않은 노드라면
    if graph[x][y] == 1:
        # 노드 방문했다고 처리
        graph[x][y] = 0
        summ += 1
        # 주변 확인하면서 방문하지 않은 노드 확인
        dfs(x-1, y) 
        dfs(x, y-1) 
        dfs(x, y+1) 
        dfs(x+1, y)
        return True
    return False
for i in range(s):
    for j in range(s):
        # dfs 
        if dfs(i,j) == True:
            # 총 블록 수 count
            result += 1
            # 장애물 수 확인
            temp.append(summ)
            summ = 0
# 총 블록 출력
print(result)
# 장애물의 수 오름차순 정렬
temp.sort()
for i in temp:
    print(i)
