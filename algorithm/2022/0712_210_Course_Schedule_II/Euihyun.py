# 못풀었습니다..
# 그래프 생성해서 돌아가면서 필요한 애들먼저 정답값으로 만들어두는 형태로 구현 하려고 했는데 구현이 어려워서..
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #그래프 생성
        graph = {}
        # 코스만큼 그래프 생성
        for i in range(numCourses):
            graph[i] = []
        # 필요한 선수과목 채우기
        for sub in prerequisites:
            a, b = sub
            graph[a].append(b)
            
