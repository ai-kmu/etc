######### 1,2번 실패 ###########
# def getStart(start, tickets, path):
#     temp = []
#     for i in range(len(tickets)):
#         if start in tickets[i][0]:
#             temp.append(tickets[i][1])
#             del tickets[i]
#             break
#     return temp

# def solution(tickets):
#     answer = []
#     middle = []
#     tickets.sort()
#     # 가장 처음은 "ICN"
#     start = "ICN"
#     path = len(tickets) + 1
    
#     for l in range(len(tickets)):
#         answer.append(start)
#         middle = getStart(start, tickets, path)
#         start = middle[0]
        
#     answer.append(start)
#     return answer

### 이중 반복문으로 코드 과다 실행### 
def DFS(start, tickets, dist, answer):
    stack = []
    
    stack.append(start)
    answer.append(start)
    
    for i in range(len(tickets)):
        temp = stack.pop()
        for i in range(len(tickets)):
            if temp in tickets[i][0]:
                if len(DFS(tickets[i][1], tickets, dist, answer)) != dist:
                    return none
                index = i
                break
        if temp not in answer:
            answer.append(temp)
            stack.extend(tickets)
    return answer

def solution(tickets):
    answer = []
    tickets.sort()
    dist = len(tickets) + 1
    DFS("ICN", tickets, dist, answer)
    
    return answer

############ 정답 ##########
def DFS(start, tickets, answer, dist, visited, stuck):
    answer.append(start)
    if(len(answer) == dist):
        stuck = False
        return stuck
    
    for i in range(len(tickets)):
        if start in tickets[i][0] and visited[i] == False and stuck == True:
            visited[i] = True
            DFS(tickets[i][1], tickets, answer, dist, visited, stuck)
            if len(answer) == dist:
                stuck = False
                return stuck
            # 만약 개수가 맞지 않다면 방문 안한걸로 변경
            visited[i] = False
            
    answer.pop()
    stuck = True
    return stuck

def solution (tickets):
    answer = []
    tickets.sort()
    visited = [False for i in tickets]
    start = "ICN"
    dist = len(tickets) + 1
    stuck = True
    
    DFS(start, tickets, answer, dist, visited, stuck)
    
    return answer