def solution(tickets):    
    def DFS(src, tickets):
        if not tickets:
            return
        
        # src가 있는 ticket에 대한 dictionary 설정
        # 1) 알파벳 순서가 앞서는 곳을 체크하고
        # 2) 해당 ticket의 index를 같이 받아서 pop함
        temp = {}
        for i, ticket in enumerate(tickets):
            if ticket[0] == src:
                temp[ticket[1]] = i
        
        # 오류의 원인: src에 해당하는 dst가 없는 경우
        if not len(temp):
            # 아까 넣었던 티켓을 지금 쓰면 안 됨
            # 따라서 그거 빼내서 remained에 넣어놓고
            dst = answer.pop()
            remained.append([answer[-1], dst])
            # 그 전부터 다시 진행
            DFS(answer[-1], tickets)
        else:
            # 1) 알파벳 순으로 정렬
            temp = sorted(temp.items(), key=lambda x:x[0])
            ticket, ind = temp[0]
            # answer에 도착지만 추가하고
            answer.append(ticket)
            # 해당 ticket은 pop
            tickets.pop(ind)
            # DFS 진행
            DFS(ticket, tickets)
    
    answer = ["ICN"]
    remained = []
    DFS("ICN", tickets)
    
    # 남아 있는 거 넣기
    if len(remained):
        DFS(answer[-1], remained)
        
    return answer
