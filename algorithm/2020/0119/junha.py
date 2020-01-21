visited = []

def dfs(computers,start,n):
    global visited
    stack = [start]     # DFS의 첫 시작, 컴퓨터부터 차례차례 리스트에 집어 넣는다. 이 리스트를 Q로 사용한다.
    while stack:
        node = stack.pop()  # 가장 앞 원소 빼와서
        visited[node] = 1   # 방문했다고 체크해준다. 1로 바꾸면 다시는 0으로 바꾸지 않는다. 
        for i in range(n):  # 모든 컴퓨터와 line7에서 빼낸 node와 연결이 되어 있는지 확인한다. 
            if computers[node][i] ==1 and visited[i] is not 1:  # 단순히 연결되어 있는지만 확인하는 것이 아니라, 이미 방문했었는지도 확인한다.
                stack.append(i) #   연결이 되어 있다면, stack list에 채워 넣는다. 



def solution(n, computers):
    global visited
    visited = [0]*n #n개의 리스트를 만든다. n번째 자리의 요소가 0이면 방문안함. 1이면 이미 방문함. 이다. 
    answer = 0  
    for i in range(n):
        if visited[i] == 0: #방문을 안했다면 
            dfs(computers, i, n)    # 사실은 i값만 보낸다. 즉 DFS 시작 컴퓨터 번호만 보낸다. 
            answer += 1
    return answer