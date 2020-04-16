import numpy as np

def solution(food_times, k):
    if sum(food_times) <= k:               # 음식 값들 합보다 k가 작거나 같은 경우
        return -1
    
    answer = -1
    fts = np.array(food_times)
    fts.sort()                             # 오름차순 정렬
    baseline = 0                           # 다 먹은 food 값 기준
    ex_move = 0                            # 마지막으로 다 먹은 값의 index
    total = fts.size
    
    for i in range(total-1):               # 마지막꺼까지 비교
        if fts[i+1] == fts[i]:             # 다음 값과 같으면 continue
            continue
        
        window = fts[i] - baseline         # 몇바퀴도는지
        lives = total - ex_move            # 현재 살아있는 food 갯수
        k -= window * lives                # 움직인 것만큼 k 값 계산
        
        if k < 0:                          # k가 -인경우
            k = (k+ (window*lives)) % lives   # k 원상복귀
            break
        elif k == 0:                       # k가 정확히 0인경우
            baseline = fts[i]              # baseline만 전달
            break
            
        baseline = fts[i]
        ex_move = i+1
        
    
    lives = total - ex_move                # lives 갱신
    baseline += k // lives                 # baseline 갱신
    k = k %lives                           # k 갱신
    
    for _ in range(2):                     # 남은 K만큼 baseline과 비교하면서 idx 찾기
        for idx, food in enumerate(food_times):
            if food > baseline:
                k -= 1
                if k == -1 :            
                    answer = idx + 1
                    return answer

    return answer
