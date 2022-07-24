import copy
def solution(tickets):
    
    # 도착지를 기준으로 정렬
    tickets.sort(key = lambda x : x[1])
    
    # 사용한 티켓(= visited)
    used = [0 for _ in tickets]
    
    answer = []
    
    def travel_path(ticket_num=-1, used=used, path=['ICN']):
        nonlocal answer
        # 방문처리 & path에 추가
        if ticket_num != -1:
            used[ticket_num] = 1
            path.append(tickets[ticket_num][1])
            
        # 정답을 찾았으면 종료
        if answer:
            return
        
        # answer 만들기(정렬 후 dfs를 진행하였기 때문에 첫번째 도달한 answer이 답이다)
        if sum(used) == len(used):
            answer = path
            return
            
        departure = path[-1]

        # 탐색
        for ticket_num, ticket in enumerate(tickets):
            ticket_departure = ticket[0]
            ticket_destination = ticket[1]
            # 출발지와 티켓의  출발지와 같고, 방문하지 않았으면
            if ticket_departure == departure and used[ticket_num] == 0:
                new_used = copy.deepcopy(used)
                new_path = copy.deepcopy(path)
                travel_path(ticket_num, new_used ,new_path)
    
    travel_path()
    return answer
