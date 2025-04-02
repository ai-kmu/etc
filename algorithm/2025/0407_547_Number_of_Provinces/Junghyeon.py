# DFS로 풀이
# Union Find? 몰루?

from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 이미 연결된 놈이면 False 리턴, 처음이면 True 리턴
        def DFS(idx):
            if visited[idx]:
                return False
            else:
                visited[idx] = True
                for i in graph[idx]:
                    DFS(i)
                return True
      
        graph = defaultdict(list)
        city_num = len(isConnected[0])

        for i in range(city_num):
            graph[i] = []

        for i in range(city_num):
            for j in range(i+1, city_num):
                # print(i, j)
                # print(isConnected[i][j])
                
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [False] * city_num

        result = 0

        for k, v in graph.items():
            if DFS(k):
                result += 1
                
        return result
