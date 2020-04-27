olution(n, t, m, timetable):
    answer = ''
    timetable = sorted(timetable)
    # 셔틀 시간대 만들어주기
    shuttle_time = []
    for i in range(n):
        time = str(9+(i*t)//60).zfill(2)+":"+str(0+(i*t)%60).zfill(2)
        shuttle_time.append(time)
    
    # 셔틀 시간대에 탄 크루 수 저장할 리스트
    shuttle_count = [0] * n
    
    # 현재 셔틀 시간 index
    curr_idx = 0
    # 탈 수 있는 마지막 승객의 timetable 시간
    con_last_time = ''
    for i in range(len(timetable)):
        # 현재 승객이 마지막 셔틀보다 늦게 온다? 그럼 그 뒤 사람들 다 못탐. 콘은 셔틀시간에 와도 됌
        if timetable[i] > shuttle_time[-1]:
            con_last_time = timetable[i]
            break  
            
        if timetable[i] <= shuttle_time[curr_idx]:
            shuttle_count[curr_idx] += 1
        else: # 현재 셔틀시간이 꽉차지 않았는데 다음 사람은 늦게 올때
            curr_idx += 1
            # 근데 그 다음 시간이 없다면? 다음 사람은 못타는 거임 콘이 타면 됌
            if curr_idx == n:
                return shuttle_time[-1]
            # 다음시간이 있다면 추가해주면 됌
            shuttle_count[curr_idx] += 1
            
        # 수용인원이 꽉 찼으면 다음 버스로 넘어가야함
        if shuttle_count[curr_idx] == m:
            curr_idx += 1
            # 다음 버스가 없음? 그럼 전 승객보다 1분 먼저타야함
            if curr_idx == n:
                con_last_time = timetable[i-1]
                break
            
        # 마지막 셔틀 시간에서 자리가 한자리 남았을 때
        if shuttle_count[-1] == m-1:
            # i가 끝까지 갔을 때도 한자리가 남았으면 셔틀시간에 맞춰서 도착가능
            if i == len(timetable)-1:
                return shuttle_time[-1]    
            # i가 끝까지 가지 않고 사람들이 남았을 때는 다음사람보다 1분 빨리오면 된다.
            else: con_last_time = timetable[i+1]
            break
    
    
    # for문이 다 끝났을 때
    if con_last_time == '':
        con_last_time = timetable[-1]
    
    # 마지막 승객의 시간이 마지막 셔틀시간보다 늦을 경우는 못탄다는 뜻이므로 콘은 셔틀시간에 맞춰서 와도 됌
    if con_last_time > shuttle_time[-1]:
        answer = shuttle_time[-1]
    # 마지막 승객이 셔틀시간보다 빠를경우는 콘이 마지막 승객보다 1분 빨리 와야 됌
    else:
        minute = con_last_time[-2:]
        if minute == '00':
            answer = str(int(con_last_time[:2])-1).zfill(2)+":"+"59"
        else:
            answer = con_last_time[:3]+str(int(minute)-1).zfill(2)
    
    return answer
