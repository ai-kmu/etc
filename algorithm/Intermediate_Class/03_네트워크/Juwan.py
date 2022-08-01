def solution(n, computers):
    
    def dfs(idx, row):
        
        if row[idx] == 0:
            return 
        
        row[idx] = 0 # 방문 처리 
        adj = [i for i in range(n) if row[i] != 0] # 연결된 노드의 인덱스를 반환
        
        if len(adj) == 0: # 만약 더 이상 갈 곳이 없으면 리턴
            return            
        
        for i in adj:
            dfs(i, computers[i]) # 연결된 노드들에 대해서 Dfs 수행
    
    ans = 0
    
    for i, node in enumerate(computers):
        
        if node[i] != 0: # 만약 아직 방문안했으면 dfs 수행
            dfs(i, node)
            ans += 1
    
    return ans
