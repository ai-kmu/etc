class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(i):
            for i_g in graph[i]:                # 엣지타고가서 한단계 더 깊게 확인
                if i_g in color:                # 색깔이 칠해져있는지 확인
                    if color[i_g]==color[i]:    # 색깔이 같은지 확인
                        return False
                else:
                    color[i_g] = 1 - color[i]   # 색깔 다르게 칠하기
                    if dfs(i_g)==False:         # 한단계 더 깊게들어가기
                        return False
            return True
        
        len_g = len(graph)
        color = defaultdict(int)
        for i in range(len_g):
            if color[i]==0:
                color[i] = -1               # 시작할때 색깔 칠하기
                if dfs(i)==False:
                    return False            # 색깔이 같게 칠해져있으면 실패
        return True
