def solution(tickets):
    t = {}
    for i in tickets:
        tmp = i[0] +i[1]
        if tmp not in t:
            t[tmp] = 1
        else:
            t[tmp] += 1
    
    graph = {}
    
    for i in tickets:
        if i[0] in graph:
            graph[i[0]].append(i[1])
        else:
            graph[i[0]] = [i[1]]
            
    max_depth = len(tickets)
    
    answer = []
    
    def dfs(depart, arrival, path, valid, depth):
        
        now_path = depart + arrival
        if now_path in valid and valid[now_path] != 0:
            valid[now_path] -= 1
            depth += 1
            if depth == max_depth:
                answer.append(path+arrival)
            
            if arrival in graph:
                for i in graph[arrival]:
                    temp = valid.copy()
                    dfs(arrival, i, path+arrival, temp, depth)
        
    
    for i in graph['ICN']:
        val = t.copy()
        dfs('ICN', i, 'ICN', val, 0)
    answer.sort()
    answer = answer[0]
    
    length = 3
    
    ans = [answer[i:i+length] for i in range(0, len(answer), length)]
    
    return ans
    
