import heapq
from collections import deque

def solution(jobs):

    heapq.heapify(jobs)
    jobs_num = len(jobs)
    sum_jobs = 0
    start, end = 0, 0
    heap = []
    
    while jobs or heap:
        while jobs and start <= jobs[0][0] <= end:
            input_t, work = heapq.heappop(jobs)
            heapq.heappush(heap, (work, input_t))
        
        if heap:
            work, input_t = heapq.heappop(heap)
            start = end
            end += work
            sum_jobs += (end-input_t)
        else:
            input_t, work = heapq.heappop(jobs)
            start = input_t
            end = start + work
            sum_jobs += (end - start)
            
    answer = (sum_jobs//jobs_num)
    
    return answer
