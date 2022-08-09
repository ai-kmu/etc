'''
jobs를 heapify하면 시작 시간이 가장 작은 순서대로 heap에 넣어진다
흐른 시간보다 시작하는 시간이 작은 작업에 대해 h에 따로 힙의 형태로 넣어준다
이때 소요 시간을 기준으로 넣어주게 되면 같은 시간대에 가장 작은 시간이 소요되는 작업을 꺼낼 수 있다
'''

import heapq

def solution(jobs):
    answer = 0
    time = 0
    h = []
    cnt = len(jobs)
    
    heapq.heapify(jobs) 
    
    while jobs or h:    
        
        while jobs:
            # 작업의 시간이 현재 시간보다 작거나 같을 경우 힙 h에 작업 소요시간과 해당 작업 정보를 넣어준다
            if jobs[0][0] <= time:
                heapq.heappush(h, (jobs[0][1], jobs[0]))
                heapq.heappop(jobs)
            else:
                break
                
        # h에 값이 들어있다면 h에서 작업 정보를 pop하고 없다면 jobs에서 pop한다
        if h:
            pick = heapq.heappop(h)[1]
        else:
            pick = heapq.heappop(jobs)
        
        # 시작될 작업이 현재 시간보다 늦는 경우
        if time < pick[0]: 
            # 현 시간을 시작될 작업의 시작시간과 소요시간을 더해서 구해준다
            # 요청부터 완료까지의 시간을 구하기 위해 소요된 시간을 answer에 더한다
            time = (pick[0] + pick[1])
            answer += pick[1]
        # 시작될 작업이 현재 시간이나 보다 이전에 요청되었을 경우
        else:
            # 바로 작업이 시작될 것이기 때문에 현재 시간을 구하기 위해 소요 시간을 더해준다
            # 요청부터 완료까지의 시간을 구하기 위해 전체시간에서 시작시간을 빼준 후 더한다
            time += pick[1] 
            answer += (time - pick[0])
            
    # 평균을 내기 위해 전에 저장해뒀던 총 요청 횟수로 나눈다
    return answer // cnt
