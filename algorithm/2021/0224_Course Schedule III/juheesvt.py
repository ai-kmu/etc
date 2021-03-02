import heapq

# heapq : 파이썬의 "보통 리스트"를 마치 최소 힙처럼 다룰 수 있도록 도와줌. PriorityQueue 처럼 별도의 자료구조가 아님.

class Solution(object):
    def scheduleCourse(self, courses):
        
        # courses 리스트를 d의 오름차순으로 정렬하기
        courses.sort(key=lambda t_end: t_end[1])

        max_heap = []
        now = 0
        
        for time, end in courses:
            now += time
            
            # max_heap인데, 기본적으로 heapq는 min_heap으로 지원하므로, (-) 부호 붙여서 넣기
            heapq.heappush(max_heap, -time)
        
            # 기간을 초과해서 강의를 들을 경우 힙에서 삭제하기
            if now > end:
                now += heapq.heappop(max_heap)

        return len(max_heap)
