from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # bipartite : 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프.
        # input : 한 인덱스와 인접한 노드들을 보여주는 리스트.
        
        colors = [0] * len(graph) # 노드마다 색깔 지정할 리스트 생성
        for i,adj in enumerate(graph):
            if colors[i]: # 한 노드가 색깔이 이미 있으면 for문 바로 다음으로 넘어감
                continue
            colors[i] = -1 # 노드에 색깔 없으면 색칠
            now = deque([i])
            while now: # 한 노드에 인접한 노드들을 조사. 서로 이미 같은 컬러이면 false 출력. 
                crit = now.popleft()
                color = colors[crit]
                for j in adj:
                    if colors[j] and colors[j] == color:
                        return False
                    elif not colors[j]:
                        colors[j] = -color
                        now.append(j)
                        
        return True
