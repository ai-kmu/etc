def solution(tickets):
    path = dict()
    # 각 항공권을 딕셔너리를 통해 표현
    for i in tickets:
        if i[0] not in path:
            path[i[0]] = []
            path[i[0]].append(i[1])
        else:
            path[i[0]].append(i[1])
    
    # 항공권의 도착지를 내림차순으로 정렬
    # DFS를 하기 위함
    for key in path:
        path[key].sort(reverse=True)
    
    ans = []
    Q = ['ICN']
    
    # DFS 수행
    while Q:
        start = Q[-1]
        
        # test case 1과 같이 현재 공항이 출발지에 없을 경우 예외처리
        # ex) IAD 공항
        if start not in path:
            ans.append(Q.pop())
            continue
        
        # 만약 현재 출발지 공항의 딕셔너리가 비어있다면 
        # ans에 Q를 pop해서 추가해줌
        if not path[start]:
            ans.append(Q.pop())
        
        # 현재 출발지 공항의 딕셔너리가 있는 상태라면
        # Q에 딕셔너리의 값을 pop해서 Q에 넣어줌
        else:
            Q.append(path[start].pop())
            
    # ans를 역순으로 정렬
    return ans[::-1]
