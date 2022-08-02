def solution(n, computers):
    answer = 0  
    # 방문체크용 리스트 선언
    visit = [0] * n

    def dfs(node):
        # 방문 체크
        visit[node] = 1
        # 해당 컴퓨터 연결 탐색
        for i,key in enumerate(computers[node]):
            # 방문 안했고 연결되어있으면 계속 타고간다.
            if key == 1 and visit[i] == 0:
                dfs(i)

    while 1:
        # 방문 다 할 때까지 conut
        if 0 in visit:
            dfs(visit.index(0))
            answer += 1
            continue
        break
    
    return answer
