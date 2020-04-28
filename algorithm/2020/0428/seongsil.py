def solution(n, t, m, timetable):
    answer = ""
    
    timetable.sort()
    
    ind_last_crew = 0
    
    # 셔틀 테이블 생성
    shuttle_time_table= ["09:00"]
    for i in range(1,n):
        shuttle_time_table.append(get_time_table(i*t))
        
    for i in range(0,n): # 셔틀 수
        for j in range(0,m): # 셔틀 수용인원 수
            if len(timetable) <= ind_last_crew: # 끝까지 모두 탈 수 있었으면 마지막에 타면 됨
                ind_last_crew = -1
                break
                
            shuttle_time = shuttle_time_table[i]
            crew_time = timetable[ind_last_crew]
            
            # 셔틀시간보다 빨리 왔으면 crew 태우고 아니면 stop
            if hour(crew_time) < hour(shuttle_time): 
                ind_last_crew += 1
            elif hour(crew_time) == hour(shuttle_time):
                if minute(crew_time) <= minute(shuttle_time):
                    ind_last_crew += 1
                else:
                    break
            elif hour(crew_time) > hour(shuttle_time):
                break
                
    if ind_last_crew <= 0 or ind_last_crew > len(timetable): # 여유있게 마지막 차 타면 되는 경우
        answer = '{0:02d}'.format(9 + (n-1)*t // 60) + ':' + '{0:02d}'.format(((n-1) * t) % 60)
    else:
        temp_last_shuttle = timetable[ind_last_crew - 1] # 마지막 crew보다 1분 빨리 와야 함
        if minute(temp_last_shuttle) > 0:
            answer = '{0:02d}'.format(hour(temp_last_shuttle)) + ':' + '{0:02d}'.format(minute(temp_last_shuttle) -1)
        if minute(temp_last_shuttle) == 0:
            answer = '{0:02d}'.format(hour(temp_last_shuttle) - 1) + ':' + '{0:02d}'.format(59)
    return answer

def get_time_table(x):
    if x < 60:
        return '{0:02d}'.format(9) + ':' + '{0:02d}'.format(x)
    else:
        return '{0:02d}'.format(9 + (x//60)) + ':' + '{0:02d}'.format(x % 60)
    
def hour(time):
    return int(time.split(':')[0])

def minute(time):
    return int(time.split(':')[1])
