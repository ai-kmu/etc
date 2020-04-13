## 오답
def solution(food_times, k):
    # food_times의 합이 k보다 작으면 -1을 return
    if sum(food_times) <= k:
        return -1
    
    # index와 times를 담을 리스트
    food_idx_and_times = []
    for i, times in enumerate(food_times):
        food_idx_and_times.append([times, i])
    
    # times의 오름차순으로 정렬
    food_idx_and_times = sorted(food_idx_and_times)
    
    # k에서 빼주는 값들을 축적할 변수
    before = 0
    # k에서 빼줄 time의 index를 담을 변수
    before_idx = 0
    
    while True:
        # time이 가장 적은 것을 뽑아서 min_time과 before_idx에 담음
        min_time, before_idx = food_idx_and_times.popleft()
        before = min_time * (len(food_idx_and_times)+1)
        # k가 빼줄 값보다 작으면 break
        if k < before:
            food_idx_and_times.append([min_time, before_idx])
            break
        # k가 더 크다면 before을 빼줌
        k -= before
    # index를 기준으로 food_idx_and_times를 정렬해줌
    food_idx_and_times = sorted(food_idx_and_times[1])
    
    # 남은 k초
    answer = k // len(food_idx_and_times)
    
    return answer

## 참고한 정답
def solution(food_times, k):
    # food_times의 합이 k보다 작으면 -1을 return
    if sum(food_times) <= k:
        return -1
    
    # index와 times를 담음
    idx_and_times = {}
    
    # time별 index 저장
    for idx, time in enumerate(food_times):
        # 만약 기존에 time이 있다면 index만 추가
        if time in idx_and_times:
            idx_and_times[time].append(idx)
        else:
            idx_and_times[time] = [idx]
    
    # food_times의 length를 담음
    length = len(food_times)
    cycle = 0
    # idx_and_times 만큼 반복
    for time in sorted(idx_and_times):
        # 만약 k가 빼줄 값보다 크다면
        if k >= length*(time-cycle):
            # k에서 빼줄 값을 빼줌
            k -= length*(time-cycle)
            # length를 빼준 time의 index들의 개수만큼 빼줌
            length -= len(idx_and_times[time])
            # 순회 횟수가
            cycle += time-cycle
        
        # 만약 k가 빼줄 값보다 작으면
        else:
            k %= length
            for i in idx_and_times:
                # 만약 time이 i보다 작으면 idx는 i
                if i >= time:
                    idx = idx_and_times[i][0]
                    break
            # idx부터 남은 k만큼 돌면서 return할 i를 찾음
            for i in range(idx, len(food_times)):
                if food_times[i] >= time:
                    if k == 0:
                        return i+1
                    k -= 1
    return -1
