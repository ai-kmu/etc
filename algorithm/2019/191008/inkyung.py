answer = []
def dfs(lst, start, route):
    global answer
    route.append(start)
    if len(lst) == 1:
        route.append(lst[0][1])
        answer.append(route)
        return answer
    for t in lst:
        if t[0] == start:
            lst_copy = lst.copy()
            lst_copy.remove(t)
            dfs(lst_copy, t[1], route.copy())
    
def solution(tickets):
    dfs(tickets, "ICN", [])
    answer.sort()
