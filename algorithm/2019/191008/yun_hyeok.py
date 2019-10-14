def dfs(tickets, start, visited, count):    
    route = [start]
    
    if count == len(tickets):
        return route, True
    
    for i in range(len(tickets)):
        from_, dest = tickets[i]
        if visited[i] or from_ != start:
            continue
        visited[i] = True
        path, flag = dfs(tickets, dest, visited, count + 1)

        if flag:
            return (route + path, True)

        visited[i] = False
            
    return route, False

def solution(tickets):
    visited = [False for t in tickets]
    tickets.sort()
    
    answer, flag = dfs(tickets, "ICN", visited, 0)
    return answer
