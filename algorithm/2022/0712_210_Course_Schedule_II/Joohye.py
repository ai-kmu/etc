# 오답
# 찾아보니 prerequisite 구조 = 위상정렬(topological sort) 문제라고 합니다. 

from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        # 선수강 해야하는 과목의 수
        inDegree = {c:0 for c in range(numCourses)}
        # 선수강 과목 수강 이후 수강할 수 있는 과목코스
        outDegree= {c:[] for c in range(numCourses)}
        
        for course, prereq in prerequisites:
            inDegree[course] += 1
            outDegree[prereq].append(course)

        q = deque([])
        
        # count 가 0 이라면(선수과목이 없다면), q에 append
        for course,count in inDegree.items():
            if count == 0:
                q.append(course)
        ans = [] 
        
        # 가능한 코스 찾기..
        while q:
            cur_course = q.popleft()
            ans.append(cur_course)
            numCourses -= 1

        # return
        return ans 
                
