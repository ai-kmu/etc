from typing import List
import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # defaultdict를 활용하여 default값을 지정
        my_graph = collections.defaultdict(list)
        for cur_c, pre_c in prerequisites:
            my_graph[cur_c] += [pre_c]
        
        # default dict를 활용하지 않고 단순 dict를 썼을 때 해당하는 Key의 값이 없기 때문에 key error 발생
        # my_graph = {}
        # for cur_c, pre_c in prerequisites :
        #     if cur_c in my_graph.keys() :
        #         my_graph[cur_c].append(pre_c)
        #         break
        #     my_graph[cur_c] = [pre_c]

        # 각 노드에 상태 할당
        # 0 : 방문하지 않은 노드
        # 1 : 방문중인 노드
        # 2 : 방문했던 노드
        states = [0]*numCourses
        res = []
        for cur_c in range(numCourses):
            if states[cur_c] == 0:
                loop = self.DFS(cur_c, res, states, my_graph)
                if loop:
                    return []
        return res
    
    def DFS(self, cur, res, states, my_graph):
        # DFS 노드에 1부터
        states[cur] = 1
        for pre_c in my_graph[cur]:
            # 그 다음 노드가 1이면 루프
            if states[pre_c] == 1: 
                return True
            # 그 다음 노드가 0이면 DFS 그대로 유지
            if states[pre_c] == 0:
                if self.DFS(pre_c, res, states, my_graph):
                    return True
        # DFS가 끝나면 res에 current course 추가하고 node를 2로
        res += [cur]
        states[cur] = 2
        return False
