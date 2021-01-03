#207. Course Schedule
# directed edge를 가지는 그래프 문제로 해결하기

class Solution:
    def buildAdjacencyList(self, n, edgesList):
        adjList = [[] for _ in range(n)]
        # c2 : c1의 선행과목
        # 예를 들어, c2-c1은 그래프의 directed edge임
        for c1, c2 in edgesList:
            adjList[c2].append(c1)
        return adjList

    def canFinish(self, numCourses, prerequisites) -> bool:
        #list로 인접한 노드들을 나타내기
        adjList = self.buildAdjacencyList(numCourses, prerequisites)

        print(adjList)

        # 각 노드는 3가지 종류의 state를 가질 수 있음
        # state 0   : 아직 방문 안함
        # state -1  : 방문은 했지만 아직 그것과 이어진 노드들에 대한 체크가 진행중인 경우
        # state 1   : 해당 노드와 그 노드와 이어진 것들 모두 처리가 되었을 때
        state = [0] * numCourses # 각 노드를 방문했는지 여부 체크하기 위한 변수

        def hasCycle(v):
            if state[v] == 1: # 방문한 노드가 모두 처리된 경우
                return False
            if state[v] == -1: # 노드에 방문했는데 이미 방문한 노드인데 아직 처리중인 경우 (이 경우는 cycle이 생긴 것을 의미)
                return True

            state[v] = -1 # 처음 노드에 방문한 경우 -1로

            #해당 노드에 인접한 노드를 체크하면서 cycle이 생기는지 체크
            for i in adjList[v]:
                if hasCycle(i): # 만약 cycle이 생겼다면
                    return True

            state[v] = 1 # cycle 없이 해당 노드와 그 노드와 이어진 것들 모두 처리가 되었을 경우
            return False

        # we traverse each vertex using DFS, if we find a cycle, stop and return
        for v in range(numCourses):
            if hasCycle(v): #cycle이 생기면 False 리턴하고 이는 선행과목에 문제가 있음을 의미
                return False

        return True # cycle이 생기지 않았다면 모든 과목 수강 가능

if __name__ == '__main__':
    numCourses=2
    prerequisites=[[1,0],[0,1]]

    s=Solution()
    print(s.canFinish(numCourses,prerequisites))