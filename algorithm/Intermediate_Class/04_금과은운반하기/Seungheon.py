# 최소가 되는 시간 찾기
def solution(a, b, g, s, w, t):
    
    # 금, 은을 이동한 양을 집합으로 보았을때
    # 금과 은 은 각각의 집합이 되고
    # mineral은 교집합이된다
    # 금과 은을 모두 만족하고 교집합도 만족해야 모든 조건을 충족한 것이다 
    
    start_time = 0
    end_time = 10**(15)
    mid_time = (start_time+end_time)//2
    
    while end_time >= start_time:
        
        total_gold = 0
        total_silver = 0
        total_mineral = 0
        
        for i in range(len(g)):
            # 이동횟수 계산(처음에는 편도, 그 다음부터는 왕복시간계산)
            move_count =  (mid_time-t[i])//(t[i]*2) + 1 if mid_time >= t[i] else 0 
            total_gold += g[i] if w[i]*move_count > g[i] else w[i]*move_count
            total_silver += s[i] if w[i]*move_count > s[i] else w[i]*move_count
            total_mineral += g[i]+s[i] if w[i]*move_count > g[i]+s[i] else w[i]*move_count
            
        # 충족했으면 시간 줄이기
        if total_gold >= a and total_silver >= b and total_mineral >= a+b:
            end_time = mid_time-1
            mid_time = (start_time+end_time)//2

        # 충족하지 못했으면 시간 늘리기
        else:
            start_time = mid_time+1
            mid_time = (start_time+end_time)//2
        
    return mid_time+1
