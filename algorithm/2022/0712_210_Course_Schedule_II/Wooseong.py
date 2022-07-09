from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''예외처리: prerequisites 비어 있으면 바로 정답 return'''
        if not prerequisites:
            return list(range(numCourses-1, -1, -1))
        
        '''(after - before) graph를 dictionary로 구현'''
        graph = defaultdict(list)
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])
        
        '''
        seen[] == -1: 뭔가 문제 발생
               ==  0: 아직 안 봄
               ==  1: 문제 없음
        '''
        answer = []
        seen = [0] * numCourses
        def DFS(after):
            '''이미 본 곳이면 괜찮다고 체크 되어 있어야 함'''
            if seen[after]:
                return seen[after] == 1
            
            '''일단 문제 있다고 체크'''
            seen[after] = -1
            '''after의 before들 중에 문제가 하나라도 있으면 안됨'''
            for before in graph[after]:
                if not DFS(before):
                    return False
            '''문제 없으니 update'''
            seen[after] = 1
            answer.append(after)
            
            return True
        
        '''재귀'''
        for node in range(numCourses):
            '''하다가 문제 생기면 [] return'''
            if not DFS(node):
                return []
        
        return answer
