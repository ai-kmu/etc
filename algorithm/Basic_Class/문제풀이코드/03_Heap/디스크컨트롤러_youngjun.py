import heapq
from collections import deque

def solution(jobs):
    
    if len(jobs) == 1:
        return jobs[0][1]
    
    jobs = sorted(jobs, key = lambda x : (x[0],x[1]))
    jobs_queue = deque(jobs)
    jobs_num = len(jobs)
    sum_jobs = 0
    start, end = 0, 0
    heap = []

    while jobs_queue or heap:
        if heap:
            work, input_t = heapq.heappop(heap)
            start = end
            end += work
            sum_jobs += (end-input_t)
        else:
            input_t, work = jobs_queue.popleft()
            start = input_t
            end = start + work
            sum_jobs += (end - start)
            
        while jobs_queue and start <= jobs_queue[0][0] <= end:
            input_t, work = jobs_queue.popleft()
            heapq.heappush(heap, (work, input_t))
    
    answer = (sum_jobs//jobs_num)
    
    return answer
