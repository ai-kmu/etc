class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        # 연결된 그룹 개수 찾기 -> dfs 탐색
        # 방문했으면 방문 안함 
        mem = [ -1 for _ in range(len(isConnected))]

        def dfs(node_idx, group_idx):
            # 방문처리
            mem[node_idx] = group_idx

            for i in range(len(isConnected)):
                if isConnected[node_idx][i] == 1: # 연결되어있는 노드중에
                    if mem[i] == -1: # 탐색이 안되었으면
                        dfs(i, group_idx)
        
        # 노드 하나씩 탐색
        group_idx = 0
        for node_i in range(len(isConnected)):
            if mem[node_i] == -1: 
                dfs(node_i, group_idx)
            group_idx += 1

        return len(set(mem))
