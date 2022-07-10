from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort 사용
        ind = [0 for _ in range(numCourses)]
        result = []
        q = deque()
        
        # 진입차수 설정
        for i in range(len(prerequisites)):
            ind[prerequisites[i][0]] += 1
            
        # print(ind)
        for i in range(numCourses):
            # 진입차수가 0인 과목을 큐에 삽입
            if ind[i] == 0:
                q.append(i)
                # 더 이상 큐에 삽입되지 않도록 1을 더 빼줌
                ind[i] -= 1
        
        while q:
            n = q.popleft()
            # 이 과목부터 들어야 하므로 result에 추가
            result.append(n)
            # 선수과목을 돌아가면서 이 과목이 선수과목이였던 과목들의 진입차수를 1씩 빼줌
            for i,j in prerequisites:
                if j == n:
                    ind[i] -= 1
                    # 만약에 진입차수가 0이 되면 새롭게 큐에 삽입하고 더 이상 큐에 삽입되지 않도록 1을 더 빼줌
                    if ind[i] == 0:
                        q.append(i)
                        ind[i] -= 1
        
        # 만약에 모든 선수과목들을 다 듣지 못했다면 모든 과목을 이수할 수 없음
        for i in range(numCourses):
            if ind[i] > -1:
                return []
        # 모든 과목을 다 들은 경우에 결과를 return
        else:
            return result
