from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        
        # BFS방식을 이용(BFS는 아닌듯함,,)
        
        answer = []
        
        # index의 course를 듣기위해 충족시켜야 하는 list
        meet_list = [set() for i in range(numCourses)]
        for meet, prerequisite in prerequisites:
            meet_list[meet].add(prerequisite)
        
        # 시작 할 수 있는 course 찾아서 queue에 삽입
        queue = deque()
        for i in range(numCourses):
            if not meet_list[i]:
                queue.append(i)

        # 방문 체크 list
        visited = [0 for i in range(numCourses)]

        while queue:
            cur_course = queue.pop()
    
            if meet_list[cur_course]:
                continue
            
            for i in  range(numCourses):
                if cur_course in meet_list[i]:
                    meet_list[i].remove(cur_course)
            
            answer.append(cur_course)
            visited[cur_course] = 1

            # 방문하지 않은 course를 queue에 삽입
            for next_course in range(numCourses):
                if visited[next_course] == 0:       
                    queue.append(next_course)      
            
            # 모든 강의를 들으면 answer return
            if visited.count(0) == 0:
                return answer
        # 모든 강의를 듣지 못하면 [] return
        return []
