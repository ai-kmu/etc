def solution(a, b, g, s, w, t):
    '''
    몇 번 움직여야 할지 알 수가 없음.
    따라서 최소 = 0 / 최대 = max로 이분 탐색 진행
    이때 max = (a + b) * t * 2 = 1e9 * 1e5 * 4 = 4e14
    '''
    
    # 이분 탐색
    time_lb = 0
    time_ub = 4e14
    answer = 4e14
    while time_lb <= time_ub:
        allowed = (time_lb + time_ub) // 2
        gold = 0
        silver = 0
        total = 0
        
        # 도시 별로 계산
        for i in range(len(g)):
            city_au = g[i]
            city_ag = s[i]
            stowage = w[i]
            transit = t[i]
            
            # 주어진 시간 동안 이동 가능한 횟수 계산
            # 왕복
            move, res = divmod(allowed, (transit * 2))
            # 편도 추가
            if res >= transit:
                move += 1
            
            # 가능한 운반량 = 이동 * 무게
            carriage = move * stowage
            
            # 도시에 그보다 적게 있으면 있는 만큼만
            gold += min(city_au, carriage)
            silver += min(city_ag, carriage)
            # 두 종류를 같이 운반할 수도 있기 때문에 체크 해야됨
            total += min(city_au + city_ag, carriage)
        
        # 운반량이 a, b보다 많으면 end를 낮추고 answer 갱신
        if gold >= a and silver >= b and total >= (a + b):
            time_ub = allowed - 1
            answer = min(answer, allowed)
        # 적으면 start를 늘리기
        else:
            time_lb = allowed + 1
            
    return answer
