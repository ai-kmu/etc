import collections
import heapq

#일을 끝내야하는 기한과 일이 오래 걸리는 경우 2가지를 모두 고려해야함 
#heapq 모듈 사용해서 해결 

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        #1. 먼저 일을 끝내야하는 기한으로 sort
        courses.sort(key=lambda t_end: t_end[1])
        print(courses)
        max_heap = []
        now = 0
        
        #2. Course 돌면서 계산 
        for t, end in courses:
            now += t
            #heapq에 원소 추가 
            heapq.heappush(max_heap, -t) #-t는 가장 오래걸리는 일을 heapq에서 맨앞에 두기위해
            print(max_heap)
            if now > end: # 초과해서 일을 할 경우 
                #heapq에서 원소 삭제 
                now += heapq.heappop(max_heap)
        return len(max_heap)
