import heapq

def solution(jobs):
    # 길이를 저장한다.
    length = len(jobs)
    # 시간 순서대로 sort한다.
    jobs.sort(reverse = True)
    # 시간, 스케쥴, 스케쥴 여부, 평균
    time = 0
    sche = []
    on_sche = 0
    mean = 0
    # job이 빌때까지 스케쥴을 채운다.
    while jobs:   
        # 시간에 맞춰 heap에 넣는다.
        if jobs[-1][0] <= time:
            # 이제 요구 시간에 맞춰 넣는다.
            jobs[-1].reverse()
            heapq.heappush(sche, jobs[-1])
            del jobs[-1]
        # 스케줄이 없으면 할당한다.
        if on_sche <= 0 and sche:
            temp = heapq.heappop(sche)
            on_sche = temp[0]
            mean += time + temp[0] - temp[1]
        time += 1
        on_sche -= 1
    # job이 비었어도 스케쥴이 끝날때까지 계속한다.
    while sche:
        if on_sche <= 0:
            temp = heapq.heappop(sche)
            on_sche = temp[0]
            mean += time + temp[0] - temp[1]
        time += 1
        on_sche -= 1
    # 평균낸다.
    mean //= length
    return mean
