class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        graph[a] = b: b를 수행해야 수강할 수 있는 a
        course_order: 코스 방문 여부 저장
        courses: 수강해야할 순서 정답 저장
        '''
        
        visit = [0 for _ in range(numCourses)] 
        course_order = [[] for _ in range(numCourses)]
        courses = []
        
        for a,b in prerequisites:
            course_order[a].append(b) 
        '''
        dfs를 이용하여 수강해야 할 코스 순서를 차례대로 courses에 저장
        dfs 함수에서 하나라도 어떤 코스를 제대로 들르지 못하는 경우(visit[i] == -1) false로 출력하도록 함
        그래서 dfs에서 false가 출력되면 빈 리스트를 출력하도록 함
        visit에서 코스별로 모두 1인 경우 모두 규칙에 맞게 방문했으므로 course를 출력
        '''
        for i in range(numCourses):
            if not self.dfs(course_order, visit, i, courses):
                return [] 
            
        return courses

    def dfs(self, course_order, visit, i, courses): 
        if visit[i] == -1: 
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1 # 이거 없으면 첫번째로 검사하기도 전에 false 리턴해버리므로 -1로 표시해야 함

        for j in course_order[i]: 
            if not self.dfs(course_order, visit, j, courses):
                return False 
        visit[i] = 1 # 규칙에 의해 코스를 제대로 들르면 1로 바꿔줌
        courses.append(i)
        return True
