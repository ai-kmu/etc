# 2가지 조건을 살펴보아야 한다. 필요하다. (즉 2번의 정렬 조건이 필요)
# 1. 얼마나 걸리는지
# 2. 마감이 언제인지
# 따라서 이번에는 얼마나 걸리는지로 정렬 후(내림차순) 
# 마감일 순으로 듣는다고 가정 후에 만약 마감일 탓에 이후 강의를 듣지 
# 못한다면 가장 긴 강의를 뺴주는 방식으로 알고리즘을 진행시킬 것이다.

from queue import PriorityQueue

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda c: c[1])
        p_queue = PriorityQueue()

        current_time = 0
        for t,d in courses:
            p_queue.put(-t) # 이번 강의를 듣는다고 가정함, 내림차순으로 정렬해야 하므로 -를 붙임
            if current_time + t > d:    #만약 마감일에 걸려 못듣는다면 가장 긴 강의를 빼줌
                current_time += p_queue.get()
            current_time+=t

        return p_queue.qsize()
